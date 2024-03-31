from rest_framework import serializers
from core_apps.users.profiles.models import Profile
from core_apps.results.results.models import Results

class PlayerResultsSerializer(serializers.ModelSerializer):
    _profit_loss_USD = serializers.DecimalField(max_digits=25, decimal_places=2)
    _profit_loss = serializers.DecimalField(max_digits=25, decimal_places=2)

    class Meta:
        model = Profile
        fields = ('id', '_profit_loss_USD',"_profit_loss")

class AgentResultsSerializer(serializers.ModelSerializer):
    _profit_loss = serializers.DecimalField(max_digits=25, decimal_places=2) 
    _rake = serializers.DecimalField(max_digits=25, decimal_places=2) 
    _rb = serializers.DecimalField(max_digits=25, decimal_places=2)        
    _rebate = serializers.DecimalField(max_digits=25, decimal_places=2) 
    _agent_settlement = serializers.DecimalField(max_digits=25, decimal_places=2) 

    class Meta:
        model= Results
        fields= ("_profit_loss","_rake","_rb","_rebate", "_agent_settlement")