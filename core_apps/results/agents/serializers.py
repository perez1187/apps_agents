from rest_framework import serializers
from core_apps.users.profiles.models import Profile

class AgentListSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user',
            'agent'
        ]
