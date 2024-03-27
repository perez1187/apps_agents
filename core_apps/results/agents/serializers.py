from rest_framework import serializers
from core_apps.users.profiles.models import Profile

class AgentListSeriaizer(serializers.ModelSerializer):

    player = serializers.ReadOnlyField(source="user.username")
    agent = serializers.ReadOnlyField(source="agent.username")

    class Meta:
        model = Profile
        fields = [
            'player',
            'agent'
        ]

class PlayerResultsSerializer(serializers.ModelSerializer):
    _profit_loss_USD = serializers.DecimalField(max_digits=25, decimal_places=2)

    class Meta:
        model = Profile
        fields = ('id', '_profit_loss_USD')