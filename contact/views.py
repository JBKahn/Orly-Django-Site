from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.response import Response

from contact.serializers import ContactSerializer
from contact.forms import ContactForm, JBKahnContactForm


class ContactFormView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Contact"}


class ContactFormViewSubmit(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        form_data = ContactSerializer(self.request.DATA).data
        form = ContactForm(form_data)
        if form.is_valid():
            form.send_email()
            return Response({}, status=200)
        else:
            return Response({"errors": form.errors}, status=422)


class JBKahmContactFormViewSubmit(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        form_data = ContactSerializer(self.request.DATA).data
        form = JBKahnContactForm(form_data)
        if form.is_valid():
            form.send_email()
            return Response({}, status=200)
        else:
            return Response({"errors": form.errors}, status=422)
