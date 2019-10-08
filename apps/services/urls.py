from django.urls import path
from apps.services.views import main, generator_world, generator_company

urlpatterns = [
    path('', main, name='services_main'),
    path('generator_world/', generator_world, name='generator_world'),
    path('generator_company/', generator_company, name='generator_company')
]
