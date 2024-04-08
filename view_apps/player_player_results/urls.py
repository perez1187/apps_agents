from django.urls import path
from .views import    GraphResultsView

urlpatterns = [
    # path('player-results/',PlayerAggregateResults.as_view()),
    path('graph-results/',GraphResultsView.as_view()),

]