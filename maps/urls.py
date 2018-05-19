from django.urls import  path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MapList, ZoneList, CourseList, AuthorList

urlpatterns = [
    path('', MapList.as_view()),
    path('zones/', ZoneList.as_view()),
    path('courses/', CourseList.as_view()),
    path('authors/', AuthorList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)