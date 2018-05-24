from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PlayerList, IPList

urlpatterns = [
    path('', PlayerList.as_view()),
    path('ips/', IPList.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
