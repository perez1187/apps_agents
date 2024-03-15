from rest_framework import generics,permissions
from core_apps.results.agents.permissions import IsAgent
from .models import Nicknames
from .serializers import NicknamesListSeriaizer


class NicknamesListView(generics.ListAPIView):
    '''
    Nickanmes list
    '''
    permission_classes = [permissions.IsAuthenticated,IsAgent]    
    serializer_class = NicknamesListSeriaizer

    # overwriting query set
    def get_queryset(self):
        # https://www.django-rest-framework.org/api-guide/filtering/
        username = self.request.user
        queryset = Nicknames.objects.filter(agent__username=username)

        return queryset