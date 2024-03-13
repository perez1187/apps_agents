from rest_framework import generics,permissions
from core_apps.results.agents.permissions import IsAgent
from .models import Reports
from .serializers import AgentReportsListSeriaizer


class AgentReportsListView(generics.ListAPIView):
    '''
    Agent reports list
    '''
    permission_classes = [permissions.IsAuthenticated,IsAgent]    
    serializer_class = AgentReportsListSeriaizer

    # overwriting query set
    def get_queryset(self):
        # https://www.django-rest-framework.org/api-guide/filtering/
        username = self.request.user
        queryset = Reports.objects.filter(agent__username=username)

        return queryset