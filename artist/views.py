from django.views.generic import TemplateView


class ArtistView(TemplateView):
    template_name = 'artist.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "The Artist"}
