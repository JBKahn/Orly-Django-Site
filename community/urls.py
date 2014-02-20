from django.conf.urls import patterns, url
from community.views import CommunityView

urlpatterns = patterns('',
        url(r'^$', CommunityView.as_view(), name='community'),
)
