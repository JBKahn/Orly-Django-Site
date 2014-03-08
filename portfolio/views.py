from django.views.generic import TemplateView
from portfolio.models import BridalPortfolio, Sprite


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Bridal Portfolio", "images": self.get_images()}

    def get_images(self):
        sprite_image = Sprite.objects.get(name='bridal_portfolio').image
        return [
            {
                "big_path": ('/').join(piece.imgfile.name.split('/')[-2:]),
                "small_path": ('/').join(sprite_image.path.split('/')[-2:]),
                "title": piece.title or ' ',
                "thumbnail_height": piece.thumbnail.height,
                "thumbnail_width": piece.thumbnail.width,
                "thumbnail_offset_top": piece.thumbnail_sprite_offset_top - piece.thumbnail.height
            } for piece in BridalPortfolio.objects.order_by('position').all()
        ]
