from rest_framework import serializers
from .models import Player, IPAddress


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class IPSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPAddress
        fields = '__all__'
