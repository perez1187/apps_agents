from django.urls import path
from .views import GetUserProfile

urlpatterns = [
    path('me/',GetUserProfile.as_view(),name="GetUserProfile"),
]