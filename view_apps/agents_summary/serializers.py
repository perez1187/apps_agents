from rest_framework import serializers
from core_apps.users.profiles.models import Profile
from core_apps.results.results.models import Results
from core_apps.results.reports.models import Reports
from core_apps.results.deals.models import Clubs

class ClubListMenuSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Clubs
        fields = (
            "club",
        )     

class PlayerResultsSerializerOld(serializers.ModelSerializer):
    _profit_loss_USD = serializers.DecimalField(max_digits=25, decimal_places=2)
    _profit_loss = serializers.DecimalField(max_digits=25, decimal_places=2)

    class Meta:
        model = Profile
        fields = ('id', '_profit_loss_USD',"_profit_loss")

class AgentResultsSerializer(serializers.ModelSerializer):
    _profit_loss = serializers.DecimalField(max_digits=25, decimal_places=2) 
    _rake = serializers.DecimalField(max_digits=25, decimal_places=2) 
    _agent_rb = serializers.DecimalField(max_digits=25, decimal_places=2)        
    _agent_rebate = serializers.DecimalField(max_digits=25, decimal_places=2) 
    _agent_settlement = serializers.DecimalField(max_digits=25, decimal_places=2) 

    _player_rb = serializers.DecimalField(max_digits=25, decimal_places=2)
    _player_rebate = serializers.DecimalField(max_digits=25, decimal_places=2)
    _player_settlement = serializers.DecimalField(max_digits=25, decimal_places=2)

    _agent_earnings = serializers.DecimalField(max_digits=25, decimal_places=2)
    _agent_earnings_rb = serializers.DecimalField(max_digits=25, decimal_places=2)
    _agent_earnings_rebate = serializers.DecimalField(max_digits=25, decimal_places=2)

    class Meta:
        model= Results
        fields= (
            "_profit_loss","_rake",
            "_agent_rb","_agent_rebate", "_agent_settlement",
            "_player_rb","_player_rebate","_player_settlement",
            "_agent_earnings_rb","_agent_earnings_rebate","_agent_earnings"
        )

class ReportResultSerializer(serializers.ModelSerializer):

    _agent_income = serializers.DecimalField(max_digits=25, decimal_places=2) 
    _players_income = serializers.DecimalField(max_digits=25, decimal_places=2) 
    _agent_earn = serializers.DecimalField(max_digits=25, decimal_places=2)

    class Meta:
        model = Reports
        fields=(
            'report_date',
            "_agent_income",
            "_players_income",
            "_agent_earn"
        )

class PlayerResultSerializer(serializers.ModelSerializer):
    _profit_loss = serializers.DecimalField(max_digits=25, decimal_places=2) 
    _rake = serializers.DecimalField(max_digits=25, decimal_places=2)
    _rakeback = serializers.DecimalField(max_digits=25, decimal_places=2)
    _rebate = serializers.DecimalField(max_digits=25, decimal_places=2)  
    _player_earn = serializers.DecimalField(max_digits=25, decimal_places=2)  
    _agent_earn = serializers.DecimalField(max_digits=25, decimal_places=2)

    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Profile
        fields = (
            "user",
            "_profit_loss",
            "_rake",
            "_rakeback",
            "_rebate",
            "_player_earn",
            "_agent_earn"
        )      

class ClubResultSerializer(serializers.ModelSerializer):
    _profit_loss = serializers.DecimalField(max_digits=25, decimal_places=2) 
    # _rake = serializers.DecimalField(max_digits=25, decimal_places=2)
    # _rakeback = serializers.DecimalField(max_digits=25, decimal_places=2)
    # _rebate = serializers.DecimalField(max_digits=25, decimal_places=2)  
    # _player_earn = serializers.DecimalField(max_digits=25, decimal_places=2)  
    # _agent_earn = serializers.DecimalField(max_digits=25, decimal_places=2)            

    class Meta:
        model = Clubs
        fields = (
            "club",
            "_profit_loss",

        )     