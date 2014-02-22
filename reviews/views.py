from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy

from reviews.forms import ClientReviewForm
from reviews.models import ClientReview


class AddReviewView(FormView):
    template_name = 'reviews.html'
    form_class = ClientReviewForm
    success_url = reverse_lazy('reviews:form_submit')

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Contact", "form": ClientReviewForm(), "reviews": self.get_reviews()}

    def form_valid(self, form):
        form.send_email()
        form.save(commit=True)
        return super(AddReviewView, self).form_valid(form)

    def get_reviews(self):
        return [{'text': review.text, 'author': review.name} for review in ClientReview.objects.order_by('position').all()]


class ReviewView(TemplateView):
    template_name = 'reviews.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Reviews", "reviews": self.get_reviews()}

    def get_reviews(self):
        return [{'text': review.text, 'author': review.name} for review in ClientReview.objects.order_by('position').all()]
