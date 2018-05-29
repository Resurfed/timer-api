from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
import debug_toolbar

urlpatterns = [
    url(r'^__debug__/', include(debug_toolbar.urls)),
]
urlpatterns = format_suffix_patterns(urlpatterns)
