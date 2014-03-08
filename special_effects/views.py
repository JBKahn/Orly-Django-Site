from django.views.generic import TemplateView
from special_effects.models import SpecialEffects
from portfolio.models import Sprite


class FXPortfolioView(TemplateView):
    template_name = 'special_effects.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "FX Portfolio", "images": self.get_images()}

    def get_images(self):
        sprite_image = Sprite.objects.get(name='special_effects').image
        return [
            {
                "big_path": ('/').join(piece.imgfile.name.split('/')[-2:]),
                "small_path": ('/').join(sprite_image.path.split('/')[-2:]),
                "title": piece.title or ' ',
                "thumbnail_height": piece.thumbnail.height,
                "thumbnail_width": piece.thumbnail.width,
                "thumbnail_offset_top": piece.thumbnail_sprite_offset_top - piece.thumbnail.height
            } for piece in SpecialEffects.objects.order_by('position').all()
        ]
