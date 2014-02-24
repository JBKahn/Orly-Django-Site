from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.response import Response

from reviews.models import ClientReview
from reviews.serializers import ReviewSerializer


class ReviewView(TemplateView):
    template_name = 'reviews.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Reviews", "reviews": self.get_reviews()}

    def get_reviews(self):
        return [{'text': review.text, 'author': review.name} for review in ClientReview.objects.order_by('position').all()]


class AddReviewView(generics.ListCreateAPIView):
    queryset = ClientReview.objects.all()
    serializer_class = ReviewSerializer
