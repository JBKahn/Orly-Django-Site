from django.views.generic import TemplateView
from core.models import Sprite


class FXPortfolioView(TemplateView):
    template_name = 'special_effects.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "FX Portfolio", "images": self.get_images()}

    def get_images(self):
        return Sprite.objects.get(name='special_effects').get_sprite_data()
