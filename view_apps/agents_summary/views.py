from rest_framework.views import APIView
from django.db.models import OuterRef, Subquery, Sum, Q
from rest_framework.response import Response

from core_apps.users.profiles.models import Profile
from core_apps.results.results.models import Results
from core_apps.results.reports.models import Reports
from core_apps.results.deals.models import Clubs

from .pagination import Pagination10000
from .permissions import IsAgentAndOwner
from .serializers import (AgentResultsSerializer, ClubListMenuSerializer,
            PlayerResultSerializer, ReportResultSerializer,ClubResultSerializer)


class ClubSummaryView(APIView,Pagination10000):
    permission_classes = [IsAgentAndOwner] 

    def get(self, request, format=None):

        # clubs = Clubs.objects.all()
        clubs = Clubs.objects.filter(
            Q(results_club__report__agent=request.user),
        ).values("club").distinct()
        
        clubs_paginate = self.paginate_queryset(clubs, request, view=self)
        serializer = ClubListMenuSerializer(clubs_paginate, many=True)

        # return Response(serializer.data)
        return  self.get_paginated_response(serializer.data)     


class PlayerResults_old(APIView, Pagination10000):
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

class GraphResults(APIView):
    permission_classes = [IsAgentAndOwner] 

    def get(self, request, format=None):
        from_date = request.GET.get('from_date','2000-03-20')
        to_date = request.GET.get('to_date','2100-01-01') 
        club = request.GET.get('club')
        nickname = request.GET.get('nickname') 

        if (
                (club == None or club =="") and
                (nickname == None or nickname == "")
            ):  
            results = Reports.objects.filter(
                Q(agent__username=request.user),
                Q(report_date__range=[from_date,to_date]),            
            ).annotate(
                _agent_income=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(agent_income=Sum("agent_settlement"))
                    .values("agent_income")
                ),
                _players_income=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(players_income=Sum("player_settlement"))
                    .values("players_income")
                ), 
                _agent_earn=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(agent_earnings=Sum("agent_earnings"))
                    .values("agent_earnings")
                ),                            
            )
        elif (
                (club != None and club !="") and
                (nickname == None or nickname == "")            
        ):   
            results = Reports.objects.filter(
                Q(agent__username=request.user),
                Q(report_date__range=[from_date,to_date]),  
                Q(results_report__club=club)          
            ).annotate(
                _agent_income=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(agent_income=Sum("agent_settlement"))
                    .values("agent_income")
                    .filter(
                        # Q(nickname_fk__nickname=nickname),
                        Q(club=club)                        
                    )                        
                ),
                _players_income=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(players_income=Sum("player_settlement"))
                    .values("players_income")
                    .filter(
                        # Q(nickname_fk__nickname=nickname),
                        Q(club=club)                        
                    )                        
                ), 
                _agent_earn=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(agent_earnings=Sum("agent_earnings"))
                    .values("agent_earnings")
                    .filter(
                        # Q(nickname_fk__nickname=nickname),
                        Q(club=club)                        
                    )                        
                ),                            
            )  
        elif (
                (club == None or club =="") and
                (nickname != None and nickname != "")
            ):
                # print("elif2")                             
            results = Reports.objects.filter(
                Q(agent__username=request.user),
                Q(report_date__range=[from_date,to_date]),  
                # Q(results_report__club=club) 
                Q(results_report__nickname_fk__nickname=nickname)         
            ).annotate(
                _agent_income=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(agent_income=Sum("agent_settlement"))
                    .values("agent_income")
                    .filter(
                        Q(nickname_fk__nickname=nickname),
                        # Q(club=club)                        
                    )                    
                ),
                _players_income=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(players_income=Sum("player_settlement"))
                    .values("players_income")
                    .filter(
                        Q(nickname_fk__nickname=nickname),
                        # Q(club=club)                        
                    )                        
                ), 
                _agent_earn=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(agent_earnings=Sum("agent_earnings"))
                    .values("agent_earnings")
                    .filter(
                        Q(nickname_fk__nickname=nickname),
                        # Q(club=club)                        
                    )                        
                ),                            
            )    
        elif (
                (club != None and club !="") and
                (nickname != None and nickname != "")
            ):
                # print("elif3") 
            results = Reports.objects.filter(
                Q(agent__username=request.user),
                Q(report_date__range=[from_date,to_date]),  
                Q(results_report__club=club) ,
                Q(results_report__nickname_fk__nickname=nickname)         
            ).annotate(
                _agent_income=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(agent_income=Sum("agent_settlement"))
                    .values("agent_income")
                    .filter(
                        Q(nickname_fk__nickname=nickname),
                        Q(club=club)                        
                    )
                ),
                _players_income=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(players_income=Sum("player_settlement"))
                    .values("players_income")
                    .filter(
                        Q(nickname_fk__nickname=nickname),
                        Q(club=club)                        
                    )                    
                ), 
                _agent_earn=Subquery(
                    Results.objects.filter(report=OuterRef("pk"))
                    .values("report")
                    .annotate(agent_earnings=Sum("agent_earnings"))
                    .values("agent_earnings")
                    .filter(
                        Q(nickname_fk__nickname=nickname),
                        Q(club=club)                        
                    )                    
                ),                            
            )                                             

        serializer = ReportResultSerializer(results, many=True)

        return Response(serializer.data)

class AgentResults(APIView, Pagination10000):
    permission_classes = [IsAgentAndOwner] 
    
    def get(self, request, format=None):

        from_date = request.GET.get('from_date','2000-03-20')
        to_date = request.GET.get('to_date','2100-01-01') 
        club = request.GET.get('club')
        nickname = request.GET.get('nickname')

        # print(club) 
        # print(nickname)

        if (
                (club == None or club =="") and
                (nickname == None or nickname == "")
            ):  
                # print("if")
                results = Results.objects.filter(
                    Q(nickname_fk__agent__username=request.user),
                    Q(report__report_date__range=[from_date,to_date]),
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
        elif (
                (club != None and club !="") and
                (nickname == None or nickname == "")            
        ):  
                # print("elif1")
                results = Results.objects.filter(
                    Q(nickname_fk__agent__username=request.user),
                    Q(report__report_date__range=[from_date,to_date]),
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
        elif (
                (club == None or club =="") and
                (nickname != None and nickname != "")
            ):
                # print("elif2")
                results = Results.objects.filter(
                    Q(nickname_fk__agent__username=request.user),
                    Q(report__report_date__range=[from_date,to_date]),
                    Q(nickname_fk__nickname=nickname)
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
        elif (
                (club != None and club !="") and
                (nickname != None and nickname != "")
            ):
                # print("elif3")
                results = Results.objects.filter(
                    Q(nickname_fk__agent__username=request.user),
                    Q(report__report_date__range=[from_date,to_date]),
                    Q(nickname_fk__nickname=nickname),
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
        
        agent_earnings_rb=results['_agent_rb'] - results['_player_rb']
        agent_earnings_rebate = results['_agent_rebate'] -results['_player_rebate']
        
        results["_agent_earnings_rb"] = agent_earnings_rb
        results["_agent_earnings_rebate"]=agent_earnings_rebate
       

        serializer = AgentResultsSerializer(results, many=False)

        return Response(serializer.data)

class PlayerResults(APIView, Pagination10000):
    """
    List all reports belongs to Agent,
    """
    permission_classes = [IsAgentAndOwner] 

    def get(self, request, format=None):

        from_date = request.GET.get('from_date','2000-03-20')
        to_date = request.GET.get('to_date','2100-01-01') 
        
        players =  Profile.objects.filter(
            Q(agent=request.user),
            # Q(user__report_agent__report_date__range=[from_date,to_date]),            
            ).annotate(
           _profit_loss=Subquery(               
                Results.objects.filter(nickname_fk__player__profile=OuterRef("pk"))               
               .values("nickname_fk__player__profile")
               .annotate(profit_loss=Sum("profit_loss"))
               .values("profit_loss")
               .filter(report__report_date__range=[from_date,to_date])
           ),
           _rake=Subquery(               
                Results.objects.filter(nickname_fk__player__profile=OuterRef("pk"))               
               .values("nickname_fk__player__profile")
               .annotate(rake=Sum("rake"))
               .values("rake")
               .filter(report__report_date__range=[from_date,to_date])
           ),
           _rakeback=Subquery(               
                Results.objects.filter(nickname_fk__player__profile=OuterRef("pk"))               
               .values("nickname_fk__player__profile")
               .annotate(rb=Sum("player_rb"))
               .values("rb")
               .filter(report__report_date__range=[from_date,to_date])
           ),   
           _rebate=Subquery(               
                Results.objects.filter(nickname_fk__player__profile=OuterRef("pk"))               
               .values("nickname_fk__player__profile")
               .annotate(rebate=Sum("player_adjustment"))
               .values("rebate")
               .filter(report__report_date__range=[from_date,to_date])
           ),   
           _player_earn=Subquery(               
                Results.objects.filter(nickname_fk__player__profile=OuterRef("pk"))               
               .values("nickname_fk__player__profile")
               .annotate(player_earn=Sum("player_settlement"))
               .values("player_earn")
               .filter(report__report_date__range=[from_date,to_date])
           ), 
           _agent_earn=Subquery(               
                Results.objects.filter(nickname_fk__player__profile=OuterRef("pk"))               
               .values("nickname_fk__player__profile")
               .annotate(agent_earn=Sum("agent_earnings"))
               .values("agent_earn")
               .filter(report__report_date__range=[from_date,to_date])
           ),                                              
       )


        players_paginate = self.paginate_queryset(players, request, view=self)
        serializer = PlayerResultSerializer(players_paginate, many=True)

        # return Response(serializer.data)
        return  self.get_paginated_response(serializer.data) 

class ClubResults(APIView, Pagination10000):
    permission_classes = [IsAgentAndOwner] 

    def get(self, request, format=None):

        from_date = request.GET.get('from_date','2000-03-20')
        to_date = request.GET.get('to_date','2100-01-01') 

        clubs = Clubs.objects.annotate(
           _profit_loss=Subquery(               
                Results.objects.filter(club_fk=OuterRef("pk"))               
               .values("club_fk")
               .annotate(profit_loss=Sum("profit_loss"))
               .values("profit_loss")
               .filter(
                Q(report__report_date__range=[from_date,to_date]),
                Q(report__agent=request.user),
                )
           ),            
        )

        clubs_paginate = self.paginate_queryset(clubs, request, view=self)
        serializer = ClubResultSerializer(clubs_paginate, many=True)

        # return Response(serializer.data)
        return  self.get_paginated_response(serializer.data)         