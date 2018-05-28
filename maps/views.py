from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from .models import Map, Zone, Course, Author
from .serializers import MapSerializer, ZoneSerializer, CourseSerializer, AuthorSerializer
from .filters import MapFilter, CourseFilter, ZoneFilter
from django_filters import rest_framework as filters

class MapList(generics.ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    filter_class = MapFilter


class MapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class ZoneList(generics.ListCreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    filter_class = ZoneFilter


class ZoneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_class = CourseFilter


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
