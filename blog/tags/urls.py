from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from tags.views import TagList

urlpatterns = patterns('',
    url(r'^$', TagList.as_view(), name='category-list'),
)


urlpatterns = format_suffix_patterns(urlpatterns)