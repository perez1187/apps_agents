from django.urls import path
from .views import   ResultList

urlpatterns = [
    # path('reports-list/',ReportList.as_view()),
    path('results-list/',ResultList.as_view()),
    # path('results-update/<int:pk>',ResultUpdateView.as_view()),
]