from django.shortcuts import render
from rest_framework import generics
from .models import Map, Zone, Course, Author
from .serializers import MapSerializer, ZoneSerializer
from .filters import MapFilter, ZoneFilter


class MapList(generics.ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    filter_class = MapFilter


class ZoneList(generics.ListCreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = MapSerializer
    filter_class = MapFilter


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = MapSerializer
    filter_class = MapFilter


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = MapSerializer
    filter_class = MapFilter
