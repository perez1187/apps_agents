from django.urls import path
from .views import   ReportList, ResultList

urlpatterns = [
    path('reports-list/',ReportList.as_view()),
    path('results-list/',ResultList.as_view()),
]