from rest_framework import serializers

from core_apps.settlements.models import Currency


class CurrencyListSerializer(serializers.ModelSerializer):  

    # report = serializers.ReadOnlyField(source="report.report_date")

    class Meta:
        model = Currency
        fields = (
            "id",
            "currency",
        )            