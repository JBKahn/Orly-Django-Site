from django.conf.urls import patterns, url
from artist.views import ArtistView

urlpatterns = patterns('',
        url(r'^$', ArtistView.as_view(), name='about'),
)
