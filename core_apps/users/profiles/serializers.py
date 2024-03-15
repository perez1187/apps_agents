from rest_framework import serializers
from . models import Profile

class UserProfileSeriaizer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source="user.username")
    user_id= serializers.ReadOnlyField(source="user.id")
    is_agent = serializers.BooleanField(source="user.is_agent")
    agent = serializers.ReadOnlyField(source="agent.username")


    class Meta:
        model = Profile
        fields = [
            'user',
            'user_id',
            'is_agent',
            'agent'
        ]
