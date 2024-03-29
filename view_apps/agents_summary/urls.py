from django.urls import path
from .views import  PlayerResults

urlpatterns = [
    path('player-results',PlayerResults.as_view())
]