from django.urls import path
from .views import AgentReportsListView

urlpatterns = [
    path('list/',AgentReportsListView.as_view(),name="AgentReportsListView"),
]