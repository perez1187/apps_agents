from rest_framework.views import APIView
from django.db.models import OuterRef, Subquery, Sum

from core_apps.users.profiles.models import Profile
from core_apps.results.results.models import Results

from .pagination import Pagination10000
from .permissions import IsAgentAndOwner
from . import serializers 


class PlayerResults(APIView, Pagination10000):
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
           ),
           _profit_loss=Subquery(               
                Results.objects.filter(nickname_fk__player__profile=OuterRef("pk"))               
               .values("nickname_fk__player__profile")
               .annotate(profit_loss2=Sum("profit_loss"))
               .values("profit_loss2")
           ),           
       )

        players_paginate = self.paginate_queryset(players, request, view=self)
        serializer = serializers.PlayerResultsSerializer(players_paginate, many=True)

        # return Response(serializer.data)
        return  self.get_paginated_response(serializer.data)



class AgentResultsGraph(APIView):
    pass