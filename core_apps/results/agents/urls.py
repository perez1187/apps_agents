from django.urls import path
from .views import AgentListView,AddPlayer

urlpatterns = [

    path('player-list/',AgentListView.as_view(),name="testres"),
    path('add-player',AddPlayer.as_view())
]