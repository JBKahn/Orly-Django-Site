from django.conf.urls import patterns, url
from contact.views import ContactFormView, ContactFormViewSubmit

urlpatterns = patterns(
    '',
    url(r'^$', ContactFormView.as_view(), name='form'),
    url(r'^submit/$', ContactFormViewSubmit.as_view(), name='form_submit'),
)
