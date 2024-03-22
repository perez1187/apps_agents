from django.urls import path
from .views import AgentListView,AddPlayer, PlayerResults

urlpatterns = [

    path('player-list/',AgentListView.as_view(),name="testres"),
    path('add-player',AddPlayer.as_view()),
    path('player-results',PlayerResults.as_view())
]