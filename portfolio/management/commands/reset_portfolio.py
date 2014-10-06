import os

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
from core.models import Sprite
from portfolio.models import BridalPortfolio


class Command(BaseCommand):
    help = 'Clears and populates the database with the initial portfolio images'

    def handle(self, *args, **options):
        BridalPortfolio.objects.all().delete()
        if settings.DEBUG:
            photo_dir = 'portfolio/management/commands/'
        else:
            photo_dir = '/home3/orlywald/src/Orly-Django-Site-master/portfolio/management/commands'
        for photo in os.listdir(photo_dir):
            if photo[-3:] not in ['png', 'jpg'] and photo[-4:] != 'jpeg':
                continue
            f = open('portfolio/management/commands/' + photo, 'r')
            f.seek(0)
            BridalPortfolio.objects.create(imgfile=File(f))
        Sprite.objects.get(name='bridal_portfolio').generate()
