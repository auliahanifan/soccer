from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Team, Player
 
# Create your views here.
 
@api_view(['GET'])
def view_teams(request):
 
    teams = Team.objects.all()
    results = [team.to_json() for team in teams]
    return Response(results, status=status.HTTP_201_CREATED)