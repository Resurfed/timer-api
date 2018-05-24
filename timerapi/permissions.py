from rest_framework.permissions import AllowAny
from servers.models import Server


class APIKeyRequired(AllowAny):
    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return True

        key = request.GET.get('key', None) if request.method == 'GET' else request.data.get('key', None)
        if key is None:
            return False

        try:
            Server.objects.get(key=key)
            return True
        except Server.DoesNotExist:
            return False
