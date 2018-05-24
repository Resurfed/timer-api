from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import players.views
urlpatterns = [
    path('', players.views.PlayerList.as_view()),
    path('<int:pk>', players.views.PlayerList.as_view()),
    path('<int:pk>/ips', players.views.IPList.as_view()),
    path('ips/', players.views.IPList.as_view()),
    path('ips/<int:pk>', players.views.IPDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
