from django.views.generic import TemplateView
from portfolio.models import BridalPortfolio


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Bridal Portfolio", "images": self.get_images()}

    def get_images(self):
        return [{"big_path": ('/').join(piece.imgfile.name.split('/')[-2:]), "small_path": ('/').join(piece.thumbnail.name.split('/')[-2:]), "title": piece.title or ' '} for piece in BridalPortfolio.objects.order_by('position').all()]
