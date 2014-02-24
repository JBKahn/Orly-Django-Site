from rest_framework import serializers

from reviews.models import ClientReview


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientReview
        fields = ['name', 'text']
