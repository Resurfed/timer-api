from django_filters import rest_framework as filters
from .models import Map, Zone


class MapFilter(filters.FilterSet):
    class Meta:
        model = Map
        fields = '__all__'


class ZoneFilter(filters.FilterSet):
    class Meta:
        model = Zone
        fields = '__all__'