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

class ResultUpdateSerializer(serializers.ModelSerializer):

    # result_id = serializers.IntegerField()

    class Meta:
        model = Results
        fields = [
            # "result_id",
            # "player",
            # "club",
            "player_deal_rb",
            "player_deal_adjustment",
        ]        


    def update(self, instance, validated_data):

        profit_loss = instance.profit_loss
        rake = instance.rake
        player_deal_rb=instance.player_deal_rb
        player_deal_adjustment = instance.player_deal_adjustment

        new_player_deal_rb = validated_data.get('player_deal_rb', player_deal_rb)
        new_player_deal_adjustment = validated_data.get('player_deal_adjustment', player_deal_adjustment)

        new_player_rb = rake * new_player_deal_rb
        new_player_adjustment = ((profit_loss+new_player_rb)*new_player_deal_adjustment)*(-1)
        new_player_settlement = profit_loss + new_player_rb + new_player_adjustment

        instance.player_deal_rb = new_player_deal_rb
        instance.player_deal_adjustment = new_player_deal_adjustment
        instance.player_rb=new_player_rb
        instance.player_adjustment = new_player_adjustment
        instance.player_settlement = new_player_settlement

        instance.save()
        return instance        