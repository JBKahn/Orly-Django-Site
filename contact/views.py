from django.views.generic import TemplateView


class ContactFormView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Contact"}
