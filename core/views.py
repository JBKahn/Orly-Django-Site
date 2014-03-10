from rest_framework import generics
from rest_framework.response import Response

from django.core.management import call_command
from core.models import Sprite


class GeneraetSprite(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        for sprite in Sprite.objects.all():
            sprite.generate()
        return Response({}, status=200)


class ResetBridalPortfolio(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        call_command('reset_portfolio')
        return Response({}, status=200)


class ResetSpecialEffectsPortfolio(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        call_command('reset_special_effects')
        return Response({}, status=200)


class ResetRevews(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        call_command('populate_initial_reviews')
        return Response({}, status=200)
