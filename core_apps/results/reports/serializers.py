from rest_framework import serializers
from .models import Reports
# from core_apps.users.profiles.models import Profile

class AgentReportsListSeriaizer(serializers.ModelSerializer):

    # player = serializers.ReadOnlyField(source="user.username")
    agent = serializers.ReadOnlyField(source="agent.username")

    class Meta:
        model = Reports
        fields = [
            # 'player',
            'id',
            'agent',
            'report_date',
            'description',
            'created_at',
            'updated_at'
        ]

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()