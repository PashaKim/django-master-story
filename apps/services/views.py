from django.shortcuts import render
from apps.services.utils import World, Pantheon, Event, Company, Adventure
from apps.services.utils_character import CharacterStory

pantheon = Pantheon()
world = World()
event = Event()
company = Company()
adventure = Adventure()


def main(request):
    return render(request, 'services/main.html', context={})


def generator_world(request):
    context = {'generator_type': 'мир',
               'world_assumptions': world.assumptions(),
               'gods_set': pantheon.gods_set(),
               'start_settlement': world.settlement(),
               }
    return render(request, 'services/generator/world.html', context=context)


def generator_company(request):
    context = {'player_base': world.settlement(),
               'vicinity_places': world.vicinity_list(),
               'worldwide_shocking_event': event.worldwide_shocking_event(),
               'company_them': company.theme(), 'company_genre': company.genre(),
               'adventure_goal': adventure.goal(), 'adventure_villain': adventure.villain(),
               'adventure_associate': adventure.associate(), 'adventure_patron': adventure.patron(),
               'adventure_intro': adventure.intro(), 'adventure_ending': adventure.ending(),
               }
    return render(request, 'services/generator/company.html', context=context)


def generator_character_story(request):
    Story = CharacterStory()
    context = {'backstory_dict': Story.backstory}
    return render(request, 'services/generator/character/story.html', context=context)
