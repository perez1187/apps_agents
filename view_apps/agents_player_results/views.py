from rest_framework.views import APIView
from django.db.models import OuterRef, Subquery, Sum, Q
from rest_framework import generics,permissions,status

from rest_framework.response import Response

from .pagination import Pagination10000, Pagination100
from .permissions import IsAgentAndOwner
from .serializers import AgentResultsSerializer

from core_apps.results.reports.models import Reports
from core_apps.results.results.models import Results


# player lists
# agent_deals.views.py
#  api/views/agents-deals/players-list/


class PlayerAggregateResults(APIView):
    permission_classes = [IsAgentAndOwner] 
    
    def get(self, request, format=None):

        from_date = request.GET.get('from_date','2000-03-20')
        to_date = request.GET.get('to_date','2100-01-01') 
        club = request.GET.get('club')
        # nickname = request.GET.get('nickname')
        player = request.GET.get('player','admin')


        if from_date =="":
            from_date ="2000-03-20"
        if to_date=="":
            to_date =    '2100-01-01' 
      

        #  1 club brak player brak
        if (
                (club == None or club =="") and
                (player == "admin" or player == "")
                # and (nickname == None or nickname == "")
            ):  
                # print("if")
                results = Results.objects.filter(
                    # Q(nickname_fk__agent__username=request.user),
                    Q(report__report_date__range=[from_date,to_date]),
                    # Q(club=club)
                    Q(nickname_fk__player__username=player)
                ).aggregate(
                    _profit_loss=Sum('profit_loss'),
                    _rake=Sum("rake"),
                    _agent_rb= Sum("agent_rb"),
                    _agent_rebate= Sum("agent_adjustment"),
                    _agent_settlement = Sum("agent_settlement"),
                    
                    _player_rb=Sum("player_rb"),
                    _player_rebate=Sum("player_adjustment"),
                    _player_settlement=Sum("player_settlement"),

                    _agent_earnings=Sum("agent_earnings")   
                )

                agent_earnings_rb = 0
                agent_earnings_rebate =0

        # 2, clubjest, player brak
        elif (
                (club != None and club !="") and
                (player == "admin" or player == "")
                # (nickname == None or nickname == "")            
        ):  
                # print("elif1")
                results = Results.objects.filter(
                    # Q(nickname_fk__agent__username=request.user),
                    Q(report__report_date__range=[from_date,to_date]),
                    Q(club=club),
                    Q(nickname_fk__player__username=player)
                ).aggregate(
                    _profit_loss=Sum('profit_loss'),
                    _rake=Sum("rake"),
                    _agent_rb= Sum("agent_rb"),
                    _agent_rebate= Sum("agent_adjustment"),
                    _agent_settlement = Sum("agent_settlement"),

                    _player_rb=Sum("player_rb"),
                    _player_rebate=Sum("player_adjustment"),
                    _player_settlement=Sum("player_settlement"),

                    _agent_earnings=Sum("agent_earnings")                      
                ) 
                agent_earnings_rb = 0
                agent_earnings_rebate =0          

        # 3 club nie ma, player jest
        elif (
                (club == None or club =="") and
                (player != "admin" or player != "")
                # (nickname != None and nickname != "")
            ):
                # print("elif2")
                results = Results.objects.filter(
                    Q(nickname_fk__agent__username=request.user),
                    Q(report__report_date__range=[from_date,to_date]),
                    Q(nickname_fk__player__username=player)
                    # Q(nickname_fk__nickname=nickname)
                    # Q(club=club)
                ).aggregate(
                    _profit_loss=Sum('profit_loss'),
                    _rake=Sum("rake"),
                    _agent_rb= Sum("agent_rb"),
                    _agent_rebate= Sum("agent_adjustment"),
                    _agent_settlement = Sum("agent_settlement"),
                                        
                    _player_rb=Sum("player_rb"),
                    _player_rebate=Sum("player_adjustment"),
                    _player_settlement=Sum("player_settlement"),

                    _agent_earnings=Sum("agent_earnings")   
                ) 

                if results['_agent_rb'] != None :
                    agent_earnings_rb=results['_agent_rb'] - results['_player_rb']
                    agent_earnings_rebate = results['_agent_rebate'] -results['_player_rebate']
                else:
                    agent_earnings_rb = 0
                    agent_earnings_rebate =0

        # club jest player jest
        elif (
                (club != None and club !="") and
                (player != "admin" or player != "")
                # (nickname != None and nickname != "")
            ):
                # print("elif3")
                results = Results.objects.filter(
                    Q(nickname_fk__agent__username=request.user),
                    Q(report__report_date__range=[from_date,to_date]),
                    Q(nickname_fk__player__username=player),
                    # Q(nickname_fk__nickname=nickname),
                    Q(club=club)
                ).aggregate(
                    _profit_loss=Sum('profit_loss'),
                    _rake=Sum("rake"),
                    _agent_rb= Sum("agent_rb"),
                    _agent_rebate= Sum("agent_adjustment"),
                    _agent_settlement = Sum("agent_settlement"),
                    
                    _player_rb=Sum("player_rb"),
                    _player_rebate=Sum("player_adjustment"),
                    _player_settlement=Sum("player_settlement"),

                    _agent_earnings=Sum("agent_earnings")                    
                ) 
                if results['_agent_rb'] != None :
                    agent_earnings_rb=results['_agent_rb'] - results['_player_rb']
                    agent_earnings_rebate = results['_agent_rebate'] -results['_player_rebate']
                else:
                    agent_earnings_rb = 0
                    agent_earnings_rebate =0                      
        
        
        results["_agent_earnings_rb"] = agent_earnings_rb
        results["_agent_earnings_rebate"]=agent_earnings_rebate
       

        serializer = AgentResultsSerializer(results, many=False)

        return Response(serializer.data)