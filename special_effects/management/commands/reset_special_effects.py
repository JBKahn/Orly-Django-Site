import os

from django.core.files import File
from django.core.management.base import BaseCommand
from special_effects.models import SpecialEffects


class Command(BaseCommand):
    help = 'Clears and populates the database with the initial special effects images'

    def handle(self, *args, **options):
        SpecialEffects.objects.all().delete()
        for photo in os.listdir('./special_effects/management/commands'):
            if photo[-3:] not in ['png', 'jpg'] and photo[-4:] != 'jpeg':
                continue
            f = open(os.getcwd() + '/special_effects/management/commands/' + photo, 'r')
            f.seek(0)
            SpecialEffects.objects.create(imgfile=File(f))
