from django.urls import path
from .views import CreateUsernames

urlpatterns = [
    path('create-usernames/',CreateUsernames.as_view(),name="GetUserProfile"),
]