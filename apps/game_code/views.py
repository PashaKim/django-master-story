from django.shortcuts import render
from django.views.generic.base import TemplateView
from apps.game_code.utils import Arrow, Hero

def main(request):
    return render(request, 'game_code/main.html', context={})


class StartView(TemplateView):
    template_name = 'game_code/start.html'
    map_row = [[0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0]]

    kobold_1 = {'img': 'http://www.imarvintpa.com/Mapping/Tokens/humanoids%20and%20giants/kobold.png', 'type': 0,
                'deg': 0, 'value': 'kobold_1'}
    kobold_2 = {'img': 'http://www.imarvintpa.com/Mapping/Tokens/humanoids%20and%20giants/kobold.png', 'type': 0,
                'deg': 0, 'value': 'kobold_2'}
    hero = Hero()
    hero_obj = hero.unit_dict
    arrow = Arrow()

    def get(self, request, *args, **kwargs):
        map_row = self.map_row
        context = self.get_context_data(**kwargs)
        map_row[5][4] = self.hero_obj
        map_row = self.arrow.all(map_row=map_row, unit=self.hero_obj)
        map_row[6][2], map_row[6][4] = self.kobold_1, self.kobold_2
        context['map_row'] = map_row
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        map_row = self.map_row
        map_row = self.hero.move(way=request.POST['arrow'], map_row=map_row)
        map_row = self.arrow.clear(map_row=map_row)
        map_row = self.arrow.all(map_row=map_row, unit=self.hero_obj)
        map_row[6][2], map_row[6][4] = self.kobold_1, self.kobold_2
        context['map_row'] = map_row
        return self.render_to_response(context)