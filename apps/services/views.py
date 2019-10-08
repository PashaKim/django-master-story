from django.shortcuts import render
from apps.services.utils import World, Pantheon

pantheon = Pantheon()
world = World()


def main(request):
    return render(request, 'services/main.html', context={})


def generator_world(request):
    context = {'generator_type': 'мир',
               'world_assumptions': world.assumptions(),
               'gods_set': pantheon.gods_set(),
               'place_of_adventure': world.place_of_adventure(),
               'city_name': world.city_name()}
    return render(request, 'services/generator/world.html', context=context)


def generator_company(request):
    context = {'place_of_adventure': world.place_of_adventure(),
               'city_name': world.city_name()}
    return render(request, 'services/generator/company.html', context=context)