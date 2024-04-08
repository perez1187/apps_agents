from rest_framework.views import APIView
from django.db.models import OuterRef, Subquery, Sum, Q
from rest_framework import generics,permissions,status

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .pagination import Pagination10000, Pagination100
from .permissions import IsAgentAndOwner
from .serializers import  ReportResultSerializer

from core_apps.results.reports.models import Reports
from core_apps.results.results.models import Results


# Create your views here.
class GraphResultsView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request, format=None):
        from_date = request.GET.get('from_date','2000-03-20')
        to_date = request.GET.get('to_date','2100-01-01') 
        club = request.GET.get('club')
        player = request.user
        # nickname = request.GET.get('nickname') 
        
        if from_date =="":
            from_date ="2000-03-20"
        if to_date=="":
            to_date =    '2100-01-01' 

        if (
                (club == None or club =="")
                # (nickname == None or nickname == "")
            ):  
            # print("jestem")
            results = Reports.objects.filter(
                Q(agent__username=request.user.profile.agent),
                Q(report_date__range=[from_date,to_date]),            
            ).annotate(

                _players_income=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(players_income=Sum("player_settlement"))
                    .values("players_income")
                    .filter(
                        # Q(nickname_fk__nickname=nickname),
                        # Q(club=club)                      
                        Q(nickname_fk__player__username=player)
                    )                        
                ), 
   
                _profit_loss=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(profit_loss=Sum("profit_loss"))
                    .values("profit_loss")
                    .filter(
                        # Q(nickname_fk__nickname=nickname),
                        # Q(club=club)                      
                        Q(nickname_fk__player__username=player)
                    )                        
                ), 
                _rake=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(rake=Sum("rake"))
                    .values("rake")
                    .filter(
                        # Q(nickname_fk__nickname=nickname),
                        # Q(club=club)                      
                        Q(nickname_fk__player__username=player)
                    )                        
                ),
                _player_rb=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(player_rb=Sum("player_rb"))
                    .values("player_rb")
                    .filter(
                        # Q(nickname_fk__nickname=nickname),
                        # Q(club=club)                      
                        Q(nickname_fk__player__username=player)
                    )                        
                ),   
                _player_adjustment=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(player_adjustment=Sum("player_adjustment"))
                    .values("player_adjustment")
                    .filter(
                        # Q(nickname_fk__nickname=nickname),
                        # Q(club=club)                      
                        Q(nickname_fk__player__username=player)
                    )                        
                ),                                                                                              
            )
                
        else :  
            # print("jestem")
            results = Reports.objects.filter(
                Q(agent__username=request.user.profile.agent),
                Q(report_date__range=[from_date,to_date]),            
            ).annotate(

                _players_income=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(players_income=Sum("player_settlement"))
                    .values("players_income")
                    .filter(
                        # Q(nickname_fk__nickname=nickname),
                        Q(club=club),                      
                        Q(nickname_fk__player__username=player)
                    )                        
                ), 
   
                _profit_loss=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(profit_loss=Sum("profit_loss"))
                    .values("profit_loss")
                    .filter(
                        # Q(nickname_fk__nickname=nickname),
                        Q(club=club) ,                     
                        Q(nickname_fk__player__username=player)
                    )                        
                ), 
                _rake=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(rake=Sum("rake"))
                    .values("rake")
                    .filter(
                        # Q(nickname_fk__nickname=nickname),
                        Q(club=club),                      
                        Q(nickname_fk__player__username=player)
                    )                        
                ),
                _player_rb=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(player_rb=Sum("player_rb"))
                    .values("player_rb")
                    .filter(
                        # Q(nickname_fk__nickname=nickname),
                        Q(club=club)  ,                    
                        Q(nickname_fk__player__username=player)
                    )                        
                ),   
                _player_adjustment=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(player_adjustment=Sum("player_adjustment"))
                    .values("player_adjustment")
                    .filter(
                        # Q(nickname_fk__nickname=nickname),
                        Q(club=club)  ,                    
                        Q(nickname_fk__player__username=player)
                    )                        
                ),                                                                                              
            )
                                
        serializer = ReportResultSerializer(results, many=True)

        return Response(serializer.data)                