from rest_framework import generics, filters
from .models import Player, IPAddress
from .serializers import PlayerSerializer, IPSerializer
from timerapi.permissions import APIKeyRequired, FullAccessKeyRequired


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [APIKeyRequired]
    filter_backends = (filters.SearchFilter,)
    search_fields = [field.name for field in Player._meta.fields]


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class IPList(generics.ListCreateAPIView):
    serializer_class = IPSerializer
    permission_classes = [FullAccessKeyRequired]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['player__name', 'ip', 'first_used', 'last_used']

    def get_queryset(self):
        queryset = IPAddress.objects.all()

        pk = self.kwargs['pk'] if 'pk' in self.kwargs else None
        if pk is not None:
            queryset = queryset.filter(player__id=pk)
        return queryset


class IPDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPAddress.objects.all()
    serializer_class = IPSerializer
    permission_classes = [FullAccessKeyRequired]