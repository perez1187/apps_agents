from rest_framework import serializers

from core_apps.results.reports.models import Reports
from core_apps.results.results.models import Results


class ReportResultSerializer(serializers.ModelSerializer):

    # _agent_income = serializers.DecimalField(max_digits=25, decimal_places=2) 
    _players_income = serializers.DecimalField(max_digits=25, decimal_places=2) 
    # _agent_earn = serializers.DecimalField(max_digits=25, decimal_places=2)
    _profit_loss = serializers.DecimalField(max_digits=25, decimal_places=2)
    _rake = serializers.DecimalField(max_digits=25, decimal_places=2)
    _player_rb = serializers.DecimalField(max_digits=25, decimal_places=2)
    _player_adjustment = serializers.DecimalField(max_digits=25, decimal_places=2)

    class Meta:
        model = Reports
        fields=(
            'report_date',
            # "_agent_income",
            "_players_income",
            # "_agent_earn",
            "_profit_loss",
            "_rake",
            "_player_rb",
            "_player_adjustment"
        )        