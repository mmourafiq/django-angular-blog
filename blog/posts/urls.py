from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views

urlpatterns = patterns('',
    url(r'^$', views.PostList.as_view(), name='post-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post-detail'),
)


urlpatterns = format_suffix_patterns(urlpatterns)