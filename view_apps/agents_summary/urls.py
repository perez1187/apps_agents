from django.urls import path
from .views import  PlayerResults, AgentResults

urlpatterns = [
    path('player-results',PlayerResults.as_view()),
    path('results/',AgentResults.as_view())
]