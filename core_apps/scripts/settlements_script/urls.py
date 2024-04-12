from django.urls import path
from .views import AddSettlements

urlpatterns = [
    path('upload/',AddSettlements.as_view(),name="GetUserProfile"),
]