from django.views.generic import TemplateView
from core.models import Sprite


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Bridal Portfolio", "images": self.get_images()}

    def get_images(self):
        return Sprite.objects.get(name='bridal_portfolio').get_sprite_data()
