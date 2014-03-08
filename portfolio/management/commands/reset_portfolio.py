import os

from django.core.files import File
from django.core.management.base import BaseCommand
from core.models import Sprite
from portfolio.models import BridalPortfolio


class Command(BaseCommand):
    help = 'Clears and populates the database with the initial portfolio images'

    def handle(self, *args, **options):
        BridalPortfolio.objects.all().delete()
        for photo in os.listdir('./portfolio/management/commands'):
            if photo[-3:] not in ['png', 'jpg'] and photo[-4:] != 'jpeg':
                continue
            f = open(os.getcwd() + '/portfolio/management/commands/' + photo, 'r')
            f.seek(0)
            BridalPortfolio.objects.create(imgfile=File(f))
        Sprite.objects.get(name='bridal_portfolio').generate()
