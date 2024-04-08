from django.urls import path
from .views import   SettlementList

urlpatterns = [

    path('settlements/',SettlementList.as_view()),



]