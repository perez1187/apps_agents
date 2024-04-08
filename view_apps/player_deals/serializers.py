from rest_framework import serializers

from core_apps.results.deals.models import Nicknames


class NicknameDealsSerializer(serializers.ModelSerializer):  

    player = serializers.ReadOnlyField(source="player.username")
    agent = serializers.ReadOnlyField(source="agent.username")

    class Meta:
        model = Nicknames
        fields = '__all__'