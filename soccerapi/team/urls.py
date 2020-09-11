from django.conf.urls import url
from django.urls import include
from rest_framework import  routers

from .views import TeamViewSet, PlayerViewSet

app_name = 'team'
team_router = routers.DefaultRouter()
team_router.register(r'', TeamViewSet, basename='team') 
player_router = routers.DefaultRouter()
player_router.register(r'', PlayerViewSet, basename='player') 
 
urlpatterns = [
    url(r'^team/', include(team_router.urls)),
    url(r'^player/', include(player_router.urls)),
]