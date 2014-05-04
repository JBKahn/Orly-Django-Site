from django.conf.urls import patterns, url
from contact.views import ContactFormView, ContactFormViewSubmit, JBKahmContactFormViewSubmit

urlpatterns = patterns(
    '',
    url(r'^$', ContactFormView.as_view(), name='form'),
    url(r'^submit/$', ContactFormViewSubmit.as_view(), name='form_submit'),
    url(r'^jbkahn/form_submit/$', JBKahmContactFormViewSubmit.as_view(), name='jbkahn_form_submit'),
)
