import rest_framework_filters as filters
from .models import Map, Course, Zone


class MapFilter(filters.FilterSet):
    class Meta:
        model = Map
        ordering = ['-id']
        fields = {'name': ['exact', 'in', 'startswith']}


class CourseFilter(filters.FilterSet):
    map = filters.RelatedFilter(MapFilter, field_name="map", queryset=Map.objects.all())

    class Meta:
        model = Course
        fields = {'map': ['exact', 'in']}


class ZoneFilter(filters.FilterSet):
    course = filters.RelatedFilter(CourseFilter, field_name="course", queryset=Course.objects.all())

    class Meta:
        model = Zone
        fields = {'course': ['exact', 'in']}
