from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from players import views

urlpatterns = [
    path('', views.PlayerList.as_view()),
    path('<int:pk>', views.PlayerList.as_view()),
    path('<int:pk>/ips', views.IPList.as_view()),
    path('ips/', views.IPList.as_view()),
    path('ips/<int:pk>', views.IPDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
