from django.urls import path
from apps.services.views import main, generator_world

urlpatterns = [
    path('', main, name='services_main'),
    path('generator_world/', generator_world, name='generator_world')
]
