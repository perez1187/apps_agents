from django.urls import path
from .views import ReportView, ReportList

urlpatterns = [
    path('<int:pk>',ReportView.as_view(),name="AgentReportsListView"),
    path('list/',ReportList.as_view(),name="AgentReportsListView"),

]