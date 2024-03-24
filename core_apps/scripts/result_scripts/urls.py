from django.urls import path
from .views import CreateResults

urlpatterns = [
    path('create-results/',CreateResults.as_view(),name="GetUserProfile"),
]