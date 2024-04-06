from django.urls import path
from .views import   CurrencyList

urlpatterns = [
    path('currency-list/',CurrencyList.as_view()),

]