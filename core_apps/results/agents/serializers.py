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
