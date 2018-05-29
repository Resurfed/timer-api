from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from maps import views

urlpatterns = [
    path('', views.MapList.as_view()),
    path('<int:pk>', views.MapDetail.as_view()),
    path('zones/', views.ZoneList.as_view()),
    path('zones/<int:pk>', views.ZoneDetail.as_view()),
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:pk>', views.CourseDetail.as_view()),
    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>', views.AuthorDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
