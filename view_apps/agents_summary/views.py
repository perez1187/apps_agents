from rest_framework.views import APIView
from django.db.models import OuterRef, Subquery, Sum, Q
from rest_framework.response import Response

from core_apps.users.profiles.models import Profile
from core_apps.results.results.models import Results

from .pagination import Pagination10000
from .permissions import IsAgentAndOwner
from .serializers import AgentResultsSerializer, PlayerResultsSerializer


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
        serializer = PlayerResultsSerializer(players_paginate, many=True)

        # return Response(serializer.data)
        return  self.get_paginated_response(serializer.data)



class AgentResults(APIView, Pagination10000):
    
    def get(self, request, format=None):

        from_date = request.GET.get('from_date','2000-03-20')
        to_date = request.GET.get('to_date','2100-01-01') 
        club = request.GET.get('club')

        print(from_date)
        print(to_date)
        results = Results.objects.filter(
            Q(nickname_fk__agent__username=request.user),
            Q(report__report_date__range=[from_date,to_date]),
            Q(club=club)
        ).aggregate(
            _profit_loss=Sum('profit_loss'),
            _rake=Sum("rake"),
            _rb= Sum("agent_rb"),
            _rebate= Sum("agent_adjustment"),
            _agent_settlement = Sum("agent_settlement")
        )

        # if club is not None:
        #     results.filter(club=club)

        # results_paginate = self.paginate_queryset(results, request, view=self)
        serializer = AgentResultsSerializer(results, many=False)

        return Response(serializer.data)
        # return  self.get_paginated_response(serializer.data)        