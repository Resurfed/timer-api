from rest_framework import generics
from .models import Player, IPAddress
from .serializers import PlayerSerializer, IPSerializer
from timerapi.permissions import APIKeyRequired, FullAccessKeyRequired


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    authentication_classes = APIKeyRequired


class IPList(generics.ListCreateAPIView):
    queryset = IPAddress.objects.all()
    serializer_class = IPSerializer
    authentication_classes = FullAccessKeyRequired
