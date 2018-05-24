from rest_framework import serializers
from .models import Player, IPAddress
import datetime


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class IPSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        ip = validated_data.get('ip', None)
        player = validated_data.get('player', None)

        addr, created = IPAddress.objects.update_or_create(ip=ip, player=player,
                                                           defaults={'last_used': datetime.datetime.utcnow()})

        return addr

    class Meta:
        model = IPAddress
        fields = '__all__'
