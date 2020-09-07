from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Team, Player

from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
 
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
 
# Create your views here.
 
@api_view(['GET'])
def view_teams(request):
 
    teams = Team.objects.all()
    results = [team.to_json() for team in teams]
    return Response(results, status=status.HTTP_201_CREATED)
 
# @api_view(['GET'])
# def view_teams(request):
#     if 'team' in cache:
#         # get results from cache
#         teams = cache.get('team')
#         print(teams)
#         return Response(teams, status=status.HTTP_201_CREATED)
 
#     else:
#         teams = Team.objects.all()
#         results = [team.to_json() for team in teams]
#         # store data in cache
#         cache.set("team", results, timeout=CACHE_TTL)
#         return Response(results, status=status.HTTP_201_CREATED)