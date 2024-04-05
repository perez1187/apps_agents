from django.urls import path
from .views import   NikcknamesAndDealsView, AgentPlayerList

urlpatterns = [
    path('players-list/',AgentPlayerList.as_view()),
    path('nickname-deals/',NikcknamesAndDealsView.as_view()),

]