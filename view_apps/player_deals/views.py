from rest_framework.views import APIView
from django.db.models import OuterRef, Subquery, Sum, Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core_apps.results.deals.models import Nicknames
from core_apps.users.profiles.models import Profile

# from .exceptions import TemplateExcpetion
from .pagination import Pagination100
from .permissions import IsAgentAndOwner
from .serializers import NicknameDealsSerializer

class NikcknamesAndDealsView(APIView,Pagination100):
    permission_classes = [IsAuthenticated] 

    def get(self, request, format=None):

        # player = request.GET.get('player')
        player = request.user

        # if (player == None or player == ""):

        #     nicknames = Nicknames.objects.filter(
        #         agent=request.user
        #     )
        # else:
        #     nicknames = Nicknames.objects.filter(
        #         Q(agent=request.user),
        #         Q(player__username=player)
        #     )            
        nicknames = Nicknames.objects.filter(
            # Q(agent=request.user),
            Q(player__username=player)
        )     
        # clubs = Clubs.objects.filter(
        #     Q(results_club__report__agent=request.user),
        # ).values("club").distinct()
        
        nicknames_paginate = self.paginate_queryset(nicknames, request, view=self)
        serializer = NicknameDealsSerializer(nicknames_paginate, many=True)

        # return Response(serializer.data)
        return  self.get_paginated_response(serializer.data)    