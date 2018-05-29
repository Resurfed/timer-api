from rest_framework import permissions, exceptions
from keys.models import Key


class APIKeyRequired(permissions.BasePermission):
    @staticmethod
    def get_key(request):
        key = request.META.get('HTTP_API_KEY', None)

        if key is None:
            return None

        try:
            return Key.objects.get(key=key)

        except Key.DoesNotExist:
            return None

    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return True

        key = self.get_key(request)

        if key is None:
            raise exceptions.PermissionDenied(detail='API key missing or invalid')

        return True

    def has_object_permission(self, request, view, obj):

        if request.user.is_authenticated:
            return True

        safe = request.method in permissions.SAFE_METHODS
        if safe:
            return True
        else:
            raise exceptions.PermissionDenied(detail='You do not have permissions to do this action')


class FullAccessKeyRequired(APIKeyRequired):
    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return True

        key = self.get_key(request)

        if key is not None and key.level == 2:
            return True

        raise exceptions.PermissionDenied(detail='You do not have permissions to view this content')

    def has_object_permission(self, request, view, obj):
        return True
