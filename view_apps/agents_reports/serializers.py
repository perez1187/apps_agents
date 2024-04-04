from rest_framework import serializers

from core_apps.results.reports.models import Reports
from core_apps.results.results.models import Results

class ReportsListSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Reports
        fields = (
            "id",
            "report_date",
            "description",
            "created_at"
        )    

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