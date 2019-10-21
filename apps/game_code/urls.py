from django.urls import path
from apps.game_code.views import main, StartView

urlpatterns = [
    path('', main, name='game_main'),
    path('start/', StartView.as_view(), name='game_start'),
]
