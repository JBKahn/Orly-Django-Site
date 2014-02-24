from django.conf.urls import patterns, url
from reviews.views import ReviewView, AddReviewView

urlpatterns = patterns(
    '',
    url(r'^$', ReviewView.as_view(), name='reviews'),
    url(r'^submit/$', AddReviewView.as_view(), name='form_submit'),
)
