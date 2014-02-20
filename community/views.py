from django.views.generic import TemplateView


class CommunityView(TemplateView):
    template_name = 'community.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Community"}
