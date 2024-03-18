from rest_framework import serializers
from .models import Nicknames

from django.contrib.auth import get_user_model
User = get_user_model()
# from core_apps.users.profiles.models import Profile

class NicknamesListSeriaizer(serializers.ModelSerializer):

    player = serializers.ReadOnlyField(source="player.username")
    agent = serializers.ReadOnlyField(source="agent.username")

    class Meta:
        model = Nicknames
        fields = [
            # 'player',
            'id',
            'agent',
            "player",
            'nickname',
            'club',
            'rb',
            'rebate',
            'created_at',
            'updated_at'
        ]

class NicknameSeriaizer(serializers.ModelSerializer):

    player = serializers.CharField(source="player.username")
    player_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    agent = serializers.ReadOnlyField(source="agent.username")

    class Meta:
        model = Nicknames
        fields = [
            # 'player',
            'id',
            'agent',
            "player",
            "player_id",
            'nickname',
            'club',
            'rb',
            'rebate',
            'created_at',
            'updated_at'
        ]
        # add read only fileds
        read_only_fields = (
            'id',
            'agent',
            'player',
            'club',
            'created_at',
            'updated_at'            
        )

class NicknameUpdateSeriaizer(serializers.ModelSerializer):

    player_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Nicknames
        fields = [
            "player_id",
            "club",
            'rb',
            'rebate',
        ]
