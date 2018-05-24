from rest_framework.permissions import AllowAny
from keys.models import Key


class APIKeyRequired(AllowAny):

    def get_key(self, request):
        key = request.GET.get('key') if request.method == 'GET' else request.data.get('key')

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

        return False if key is None else True


class FullAccessKeyRequired(APIKeyRequired):
    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return True

        key = self.get_key(request)

        if key is not None and key.level == 2:
            return True

        return False
