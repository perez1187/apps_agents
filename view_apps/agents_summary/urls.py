from django.urls import path
from .views import   AgentResults, GraphResults, PlayerResults,ClubResults,ClubSummaryView

urlpatterns = [
    # path('player-results/',PlayerResults.as_view()),
    path('agent-results/',AgentResults.as_view()),
    path('graph-results/',GraphResults.as_view()),
    path('player-results/',PlayerResults.as_view()),
    path('clubs-results/',ClubResults.as_view()),

    path('clubs-list/',ClubSummaryView.as_view()),
]