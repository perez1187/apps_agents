from django.urls import path
from .views import   PlayerAggregateResults

urlpatterns = [
    path('player-results/',PlayerAggregateResults.as_view()),

]