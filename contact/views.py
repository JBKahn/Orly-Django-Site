from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from contact.forms import ContactForm


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:form_submit')

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Contact", "form": ContactForm()}


class ContactFormViewSubmit(TemplateView):
    template_name = 'success.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Contact"}
