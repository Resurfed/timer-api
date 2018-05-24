from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maps/', include('maps.urls')),
    path('times/', include('times.urls')),
    path('players/', include('players.urls')),
    path('servers/', include('servers.urls')),
    path('keys/', include('keys.urls'))
]
