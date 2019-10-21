from django.urls import path
from apps.services.views import main, generator_world, generator_company, generator_character_story

urlpatterns = [
    path('', main, name='services_main'),
    path('generator_world/', generator_world, name='generator_world'),
    path('generator_company/', generator_company, name='generator_company'),
    path('generator_character_story/', generator_character_story, name='generator_character_story')
]
