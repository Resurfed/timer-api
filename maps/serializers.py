from rest_framework import serializers
from .models import Map, Zone, Course, Author


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    map = serializers.IntegerField(source='map.id', read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'context' in kwargs:
            request = kwargs['context']['request']
            verbose = request.GET.get('verbose', False)

            if verbose:
                self.fields['zones'] = ZoneSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class MapSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = kwargs['context']['request']
        verbose = request.GET.get('verbose', False)

        if verbose:
            self.fields['courses'] = CourseSerializer(many=True, read_only=True, **kwargs)

    class Meta:
        model = Map
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
