from rest_framework.response import Response
from rest_framework import status, generics, filters, permissions

from core_apps.users.profiles.models import Profile
from . import serializers


class AgentListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]    
    serializer_class = serializers.AgentListSeriaizer


    # overwriting query set
    def get_queryset(self):
        # https://www.django-rest-framework.org/api-guide/filtering/
        username = self.request.user
        queryset = Profile.objects.filter(agent__username=username)
        # username = self.request.user
        # reportDate = self.request.query_params.get('reportDate')

        # queryset = queryset.filter(ref_fk__user__username=username)

        # if reportDate is not None:
        #     queryset = queryset.filter(reportId__date=reportDate)  

        return queryset

    def list(self,request):
        # print("jeste,")
        # print(self.request.user)
        queryset = self.get_queryset()  
        results = {
            "agentResults" : {
                "by_date":agent_by_date,
                "by_club":agent_by_club
            }
        }          

        return Response(results,status.HTTP_200_OK)          