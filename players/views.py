from django.shortcuts import render
from rest_framework import generics
from .serializers import PlayerSerializer, IPAddressSerializer
from .models import Player, IPAddress


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerInfoByID(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class IPList(generics.ListCreateAPIView):

    serializer_class = IPAddressSerializer

    def get_queryset(self):
        queryset = IPAddress.objects.all()
        pk = self.kwargs['pk']
        if pk is not None:
            queryset = queryset.filter(player__id=pk)
        return queryset