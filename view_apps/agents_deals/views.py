from rest_framework.views import APIView
from django.db.models import OuterRef, Subquery, Sum, Q

from rest_framework import status
from rest_framework.response import Response

from core_apps.results.deals.models import Nicknames
from core_apps.users.profiles.models import Profile

from .exceptions import TemplateExcpetion
from .pagination import Pagination100
from .permissions import IsAgentAndOwner
from .serializers import NicknameDealsSerializer,PlayerListFromAgent, NicknameUpdateSeriaizer

# player list

class AgentPlayerList(APIView):

    permission_classes = [IsAgentAndOwner] 

    def get(self, request, format=None):
        players = Profile.objects.filter(
            agent=request.user
        )

        serializer = PlayerListFromAgent(players, many=True)

        return Response(serializer.data)

class NikcknamesAndDealsView(APIView,Pagination100):
    permission_classes = [IsAgentAndOwner] 

    def get(self, request, format=None):

        player = request.GET.get('player')

        if (player == None or player == ""):

            nicknames = Nicknames.objects.filter(
                agent=request.user
            )
        else:
            nicknames = Nicknames.objects.filter(
                Q(agent=request.user),
                Q(player__username=player)
            )            

        # clubs = Clubs.objects.filter(
        #     Q(results_club__report__agent=request.user),
        # ).values("club").distinct()
        
        nicknames_paginate = self.paginate_queryset(nicknames, request, view=self)
        serializer = NicknameDealsSerializer(nicknames_paginate, many=True)

        # return Response(serializer.data)
        return  self.get_paginated_response(serializer.data)    

class NicknameAndDealsDetailView(APIView):
    permission_classes = [IsAgentAndOwner] 

    def get_object(self, pk):

        # print(request.data["id"])
        try:
            obj =  Nicknames.objects.get(pk=pk)
        except Nicknames.DoesNotExist:
            raise Http404
        
        #  call has object permissions
        self.check_object_permissions(self.request, obj)  
        return obj               


    def put(self, request, pk, format=None):
        nickname = self.get_object(pk)
        # print(request.data["player_id"])
        try:
            obj = Profile.objects.get(
                user=request.data["player_id"]
            )
        except:
            raise TemplateExcpetion(
                detail=
                    {"error": "wrong player_id"}, 
                    status_code=status.HTTP_400_BAD_REQUEST)            
        # print(request.user.pkid)
        # print(obj.agent.pkid)
        if request.user.pkid != obj.agent.pkid:
            raise TemplateExcpetion(
                detail=
                    {"error": "wrong player_id"}, 
                    status_code=status.HTTP_400_BAD_REQUEST)  

        serializer = NicknameUpdateSeriaizer(nickname, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)