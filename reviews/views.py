from django.views.generic import TemplateView
from rest_framework import generics

from reviews.models import ClientReview
from reviews.serializers import ReviewSerializer
from core.models import Sprite


class ReviewView(TemplateView):
    template_name = 'reviews.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Testimonials", "reviews": self.get_reviews()}

    def get_reviews(self):
        return Sprite.objects.get(name='reviews').get_sprite_data()


class AddReviewView(generics.ListCreateAPIView):
    queryset = ClientReview.objects.all()
    serializer_class = ReviewSerializer
