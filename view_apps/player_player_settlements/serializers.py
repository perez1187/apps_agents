from rest_framework import serializers
from core_apps.settlements.models import Settlement


class SettlementListCreateSerializer(serializers.ModelSerializer):
    player = serializers.ReadOnlyField(source="player.username")
    agent = serializers.ReadOnlyField(source="agent.username")
    currency = serializers.ReadOnlyField(source="currency.currency")

    class Meta:
        model = Settlement
        fields = '__all__'
        # fields = [
        #     "player",
        #     "date",
        #     "transactionUSD",
        #     "transactionValue",
        #     "currency",
        #     "exchangeRate",
        #     "description"
        # ]