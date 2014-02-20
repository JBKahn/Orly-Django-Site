from django.conf.urls import patterns, url
from services.views import ServiceView

urlpatterns = patterns('',
        url(r'^$', ServiceView.as_view(), name='services'),
)
