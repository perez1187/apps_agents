from django.urls import path
from .views import   NikcknamesAndDealsView, AgentPlayerList, NicknameAndDealsDetailView

urlpatterns = [
    path('players-list/',AgentPlayerList.as_view()),
    path('nickname-deals/',NikcknamesAndDealsView.as_view()),
    path('nickname-deals-update/<int:pk>',NicknameAndDealsDetailView.as_view()),

]