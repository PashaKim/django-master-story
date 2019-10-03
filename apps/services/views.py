from django.shortcuts import render
from apps.services.utils import World


def main(request):
    return render(request, 'services/main.html', context={})


def generator_world(request):
    world = World()
    context = {'generator_type': 'мир',
               'world_assumptions': world.assumptions(),
               'gods_set': world.gods_set()}
    return render(request, 'services/generator.html', context=context)

