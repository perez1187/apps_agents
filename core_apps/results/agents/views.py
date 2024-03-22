from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status, generics, filters, permissions

from django.db.models import OuterRef, Subquery, Sum, Count

from django.contrib.auth import get_user_model
User = get_user_model()


from core_apps.users.profiles.models import Profile
from core_apps.results.results.models import Results
from . import serializers 
# from core import models
from .permissions import IsAgent
from .pagination import Pagination100



class AgentListView(generics.ListAPIView):
    '''
    Find Players conected with the Agent
    '''
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
        '''
        Add player to Agent. 
        Provide user ID
        '''

        try:
            request.data["id"]
        except:
            return Response({"error":"you need to specify ID "},status=status.HTTP_404_NOT_FOUND)
                 
        try:
            find_player = User.objects.get(id=request.data["id"])
        except:
            return Response({"error":"Player doesnt exist"},status=status.HTTP_404_NOT_FOUND)
        
        # print(find_user[0].pkid) # if we .filter
        player =Profile.objects.get(user = find_player.pk)

        if player.agent is not None:
            return Response({"error":"Player already have an agent"},status=status.HTTP_404_NOT_FOUND)

        player.agent=request.user
        player.save()

        return Response({"success":f"Player: {player.user} has been added"},status=status.HTTP_201_CREATED)

     
        

        # serializer = SnippetSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlayerResults(APIView, Pagination100):
    """
    List all reports belongs to Agent,
    """
    # permission_classes = [permissions.IsAuthenticated,IsAgentAndOwner] 

    def get(self, request, format=None):
        
        # players = Profile.objects.filter(agent=request.user)
        players =  Profile.objects.annotate(
           _profit_loss_USD=Subquery(               
                Results.objects.filter(nickname_fk__player__profile=OuterRef("pk"))               
               .values("nickname_fk__player__profile")
               .annotate(profit_loss=Sum("profit_loss"))
               .values("profit_loss")
           )
       )


        players_paginate = self.paginate_queryset(players, request, view=self)
        serializer = serializers.PlayerResultsSerializer(players_paginate, many=True)

        # return Response(serializer.data)
        return  self.get_paginated_response(serializer.data)