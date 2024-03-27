from django.urls import path
from .views import NicknamesListView, NicknameDetail
    

urlpatterns = [
    path('nicknames/',NicknamesListView.as_view(),name="NicknamesListView"),
    path('nickname/<int:pk>',NicknameDetail.as_view(),name="NicknameDetail"),    
    # path('nickname/',NicknameUpdate.as_view(),name="NicknameUpdate"), 
]