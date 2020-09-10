from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    # Use cache for speed up
    @method_decorator(cache_page(60*2))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def create(self, request, *args, **kwargs):
        many = True if isinstance(request.data, list) else False
        serializer = PlayerSerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Use cache to speed up
    @method_decorator(cache_page(60*2))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)