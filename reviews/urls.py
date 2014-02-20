from django.conf.urls import patterns, url
from reviews.views import ReviewView

urlpatterns = patterns('',
        url(r'^$', ReviewView.as_view(), name='reviews'),
)
