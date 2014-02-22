from django.views.generic import TemplateView
from special_effects.models import SpecialEffects


class FXPortfolioView(TemplateView):
    template_name = 'special_effects.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "FX Portfolio", "images": self.get_images()}

    def get_images(self):
        return [{"big_path": ('/').join(piece.imgfile.name.split('/')[-2:]), "small_path": ('/').join(piece.thumbnail.name.split('/')[-2:]), "title": piece.title or ' '} for piece in SpecialEffects.objects.order_by('position').all()]
