from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase
from .views import TeamViewSet, PlayerViewSet
from .models import Team, Player
from rest_framework import status

# import unittest

# Create your tests here.
class TeamApiTests(APITestCase):
    
    def test_create_team(self):
        base_url = reverse('team:team-list')
        data = {'name': 'Persibas Banyumas'}
        response = self.client.post(base_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(Team.objects.get().name, 'Persibas Banyumas')
    
    def test_get_teams(self):
        base_url = reverse('team:team-list')
        response = self.client.get(base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_team(self):
        base_url = reverse('team:team-list')
        response = self.client.get(base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
class PlayerApiTests(APITestCase):

    def test_create_player(self):
        Team.objects.create(name='Banyuwangi FC')
    
        base_url = reverse('team:player-list')
        data = {'name': 'Robinson', 'number': 20, 'team': 1}
    
        response = self.client.post(base_url, data, format='json')
    
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Player.objects.count(), 1)
        self.assertEqual(Player.objects.get().name, 'Robinson')
