from rest_framework import serializers

from core_apps.results.reports.models import Reports
from core_apps.results.results.models import Results


class NicknameDealsSerializer(serializers.ModelSerializer):  

    player = serializers.ReadOnlyField(source="player.username")

    class Meta:
        model = Results
        fields = (
            "id",
            "player",
            "nickname",

        )     

class PlayerListFromAgent(serializers.ModelSerializer):  

    player = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Results
        fields = (

            "player",
        )                  