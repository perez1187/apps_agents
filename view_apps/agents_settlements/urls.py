from django.urls import path
from .views import   CurrencyList, CreateSettlement, SettlementList,DeleteSettlement

urlpatterns = [
    path('currency-list/',CurrencyList.as_view()),
    path('create-settlement/',CreateSettlement.as_view()),
    path('settlements/',SettlementList.as_view()),
    path('delete/<int:pk>',DeleteSettlement.as_view()),


]