from rest_framework import serializers
from django.contrib.auth import get_user_model

from core_apps.results.reports.models import Reports
from core_apps.results.results.models import Results
from core_apps.results.deals.models import Nicknames

User = get_user_model()


class NicknameDealsSerializer(serializers.ModelSerializer):  

    player = serializers.ReadOnlyField(source="player.username")
    agent = serializers.ReadOnlyField(source="agent.username")

    class Meta:
        model = Nicknames
        fields = '__all__'
        # (
        #     "id",
        #     "player",
        #     "nickname",
        #     "nickname_id",
        #     "club",
        #     "rb",
        #     "rebate",

        # )     

class PlayerListFromAgent(serializers.ModelSerializer):  

    player = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Results
        fields = (
            "id",
            "player",
        )                  



class NicknameUpdateSeriaizer(serializers.ModelSerializer):

    player_id = serializers.IntegerField()

    class Meta:
        model = Nicknames
        fields = [
            "player_id",
            # "player",
            # "club",
            'rb',
            'rebate',
        ]

