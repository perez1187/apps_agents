from rest_framework import serializers

from core_apps.settlements.models import Currency, Settlement


class CurrencyListSerializer(serializers.ModelSerializer):  

    # report = serializers.ReadOnlyField(source="report.report_date")

    class Meta:
        model = Currency
        fields = (
            "id",
            "currency",
        )            

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