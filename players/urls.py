from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PlayerList, PlayerInfoByID ,IPList

urlpatterns = [
    path('', PlayerList.as_view()),
    path('<int:pk>', PlayerInfoByID.as_view()),
    path('<int:pk>/ips', IPList.as_view() )
]
urlpatterns = format_suffix_patterns(urlpatterns)
