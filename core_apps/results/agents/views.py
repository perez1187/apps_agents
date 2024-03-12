from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status, generics, filters, permissions

from django.contrib.auth import get_user_model
User = get_user_model()


from core_apps.users.profiles.models import Profile
from . import serializers
# from core import models
from .permissions import IsAgent



class AgentListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,IsAgent]    
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

    # def list(self,request):
    #     # print("jeste,")
    #     # print(self.request.user)
    #     queryset = self.get_queryset()  
    #     results = {
    #         "agentResults" : {
    #             "by_date":agent_by_date,
    #             "by_club":agent_by_club
    #         }
    #     }          

        return Response(results,status.HTTP_200_OK)          

class AddPlayer(APIView):
    permission_classes = [permissions.IsAuthenticated,IsAgent]

    # dodac sprawdzenie czy istnieje juz agent
    # sprawdzic pagination

    def post(self, request, format=None):
        print("taak")
        # uid = "b939361e-cc4f-49b6-b386-67bc9364e8a8"
        if request.data["id"] :
            
            try:
                find_user = User.objects.get(id=request.data["id"])
            except:
                return Response({"error":"Player doesnt exist"},status=status.HTTP_404_NOT_FOUND)
            # print(find_user[0].pkid) # if we .filter
            print(find_user.pk)
            user_profile =Profile.objects.get(user = find_user.pk)
            print(user_profile.agent)
            print(request.user)
            user_profile.agent=request.user
            user_profile.save()

        print(request.data["id"])

        return Response("yes",status=status.HTTP_201_CREATED)

        # serializer = SnippetSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


