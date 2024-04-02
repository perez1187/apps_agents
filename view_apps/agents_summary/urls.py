from django.urls import path
from .views import   AgentResults, GraphResults

urlpatterns = [
    # path('player-results/',PlayerResults.as_view()),
    path('agent-results/',AgentResults.as_view()),
    path('graph-results/',GraphResults.as_view())
]