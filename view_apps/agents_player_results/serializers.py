from rest_framework import serializers

# from core_apps.results.reports.models import Reports
from core_apps.results.results.models import Results
from core_apps.results.reports.models import Reports

class ResultListSerializer(serializers.ModelSerializer):  

    report = serializers.ReadOnlyField(source="report.report_date")

    class Meta:
        model = Results
        fields = (
            "id",
            "report",
            "club",
            "nickname",
            "nickname_id",
            "agents",
            "profit_loss",
            "rake",
            "agent_deal",
            "agent_rb",
            "agent_adjustment",
            "agent_settlement",
            "player_deal_rb",
            "player_deal_adjustment",
            "player_rb",
            "player_adjustment",
            "player_settlement",
            "agent_earnings",
            "created_at",
            "updated_at"
        )            

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
    _profit_loss = serializers.DecimalField(max_digits=25, decimal_places=2)
    _rake = serializers.DecimalField(max_digits=25, decimal_places=2)
    _player_rb = serializers.DecimalField(max_digits=25, decimal_places=2)
    _player_adjustment = serializers.DecimalField(max_digits=25, decimal_places=2)

    class Meta:
        model = Reports
        fields=(
            'report_date',
            "_agent_income",
            "_players_income",
            "_agent_earn",
            "_profit_loss",
            "_rake",
            "_player_rb",
            "_player_adjustment"
        )        