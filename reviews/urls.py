from django.conf.urls import patterns, url
from reviews.views import ReviewView, AddReviewView

urlpatterns = patterns(
    '',
    url(r'^$', AddReviewView.as_view(), name='reviews'),
    url(r'^submit/$', ReviewView.as_view(), name='form_submit'),
)
