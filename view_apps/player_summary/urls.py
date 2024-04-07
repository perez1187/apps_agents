from django.urls import path
from .views import   PlayerAggregateResultsView, GraphResults, PlayerResults,ClubResults,ClubSummaryView

urlpatterns = [
    # path('player-results/',PlayerResults.as_view()),
    path('player-aggregate-results/',PlayerAggregateResultsView.as_view()),
    path('graph-results/',GraphResults.as_view()),
    # path('player-results/',PlayerResults.as_view()),
    # path('clubs-results/',ClubResults.as_view()),

    path('clubs-list/',ClubSummaryView.as_view()),
]