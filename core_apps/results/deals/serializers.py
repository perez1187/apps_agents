from rest_framework import serializers
from .models import Nicknames
# from core_apps.users.profiles.models import Profile

class NicknamesListSeriaizer(serializers.ModelSerializer):

    player = serializers.ReadOnlyField(source="player.username")
    agent = serializers.ReadOnlyField(source="agent.username")

    class Meta:
        model = Nicknames
        fields = [
            # 'player',
            'agent',
            "player",
            'nickname',
            'club',
            'rb',
            'rebate',
            'created_at',
            'updated_at'
        ]
