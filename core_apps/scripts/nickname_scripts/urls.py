from django.urls import path
from .views import CreateNicknames

urlpatterns = [
    path('create-nicknames/',CreateNicknames.as_view(),name="CreateNicknames"),
]