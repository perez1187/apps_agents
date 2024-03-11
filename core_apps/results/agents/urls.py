from django.urls import path
from .views import AgentListView,AddPlayer

urlpatterns = [
    # path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('player-list/',AgentListView.as_view(),name="testres"),
    path('add-player',AddPlayer.as_view())
    # path('add-report-manual/',UploadFileView.as_view(),name="testres2"),
    # path('agent-result-summary/',PlayerResultsView.as_view(),name="player_results"),
    # path('agent-results-details/', Agent_raw_results_View.as_view(), name='upload-file'),
    # path('agent-results-details-summary/', Agent_raw_results_Sum_View.as_view(), name='upload-file'),
    # # path('upload_clubs/', UploadClubsView.as_view(), name='upload-file'),
]