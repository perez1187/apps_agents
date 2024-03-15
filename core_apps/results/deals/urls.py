from django.urls import path
from .views import NicknamesListView

urlpatterns = [
    path('nicknames/',NicknamesListView.as_view(),name="NicknamesListView"),
]