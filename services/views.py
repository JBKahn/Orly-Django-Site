from django.views.generic import TemplateView


class ServiceView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Services"}
