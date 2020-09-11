from rest_framework import serializers
from .models import Team, Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class PlayerForTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'number', 'id')

class TeamSerializer(serializers.ModelSerializer):
    player = PlayerForTeamSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('player', 'name', 'id', 'date_created', 'date_modified')
        read_only_fields = ['player']

    

