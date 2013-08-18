from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from tags.views import TagList, TagDetail

urlpatterns = patterns('',
    url(r'^$', TagList.as_view(), name='tag-list'),
    url(r'^(?P<pk>[0-9]+)/$', TagDetail.as_view(), name='tag-detail'),
)


urlpatterns = format_suffix_patterns(urlpatterns)