from django.views.generic.edit import FormView
from portfolio.forms import PortfolioForm
from portfolio.models import BridalPortfolio
from django.core.urlresolvers import reverse_lazy


class PortfolioView(FormView):
    template_name = 'portfolio.html'
    form_class = PortfolioForm
    success_url = reverse_lazy('portfolio:portfolio')

    def form_valid(self, form):
        newimg = BridalPortfolio(imgfile=self.request.FILES['imgfile'])
        newimg.save()
        return super(PortfolioView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Bridal Portfolio", "images": self.get_images(), "form": PortfolioForm()}

    def get_images(self):
        return [{"big_path": ('/').join(piece.imgfile.name.split('/')[-2:]), "small_path": ('/').join(piece.thumbnail.name.split('/')[-2:]), "title": "test_title"} for piece in BridalPortfolio.objects.all()]
