from django.conf.urls import patterns, include, url
from views import friends, friends_of_friends, recommendation

urlpatterns = patterns('',
    url(r'^(?P<idx>\d+)/$', friends, name='friends'),
    url(r'^friends/(?P<idx>\d+)/$', friends_of_friends, name='friends_of_friends'),
    url(r'^recommendation/(?P<idx>\d+)/$', recommendation, name='recommendation'),
)
