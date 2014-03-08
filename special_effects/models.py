import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver

from cStringIO import StringIO
from PIL import Image

from mysite.settings import STATIC_URL
from portfolio.models import Sprite


class SpecialEffects(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    imgfile = models.ImageField(upload_to=STATIC_URL[1:] + 'img')
    thumbnail = models.ImageField(upload_to=STATIC_URL[1:] + 'img', max_length=500, blank=True, null=True)
    position = models.PositiveSmallIntegerField("Position")
    thumbnail_sprite_offset_top = models.PositiveSmallIntegerField(default=0)
    sprite = models.ForeignKey(Sprite)

    class Meta:
        ordering = ['position']

    def format_thumbnail(self):
        # import ipdb; ipdb.set_trace();
        return u'<img src="/%s" />' % '/'.join(self.thumbnail.url.split('/')[1:])
    format_thumbnail.allow_tags = True

    def create_thumbnail(self):
        # original code for this method came from
        # http://snipt.net/danfreak/generate-thumbnails-in-django-with-pil/

        # If there is no image associated with this.
        # do not create thumbnail
        if not self.imgfile:
            return

        # Set our max thumbnail size in a tuple (max width, max height)
        THUMBNAIL_SIZE = (233, 1000000)

        if hasattr(self.imgfile.file, 'content_type'):
            DJANGO_TYPE = self.imgfile.file.content_type
        else:
            if self.imgfile.file.name[-3:] == 'png':
                DJANGO_TYPE = 'image/png'
            else:
                DJANGO_TYPE = 'image/jpeg'

        if DJANGO_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'image/png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'

        # Open original photo which we want to thumbnail using PIL's Image
        image = Image.open(StringIO(self.imgfile.read()))

        # Use Image.ANTIALIAS to reduce potential artifacts that may result
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
        temp_handle = StringIO()
        image.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)

        suf = SimpleUploadedFile(os.path.split(self.imgfile.name)[-1], temp_handle.read(), content_type=DJANGO_TYPE)
        self.thumbnail.save('%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENSION), suf, save=False)

    def save(self, *args, **kwargs):
        if not self.thumbnail:
            self.create_thumbnail()
        if self.position is None:
            # Append
            try:
                last = self.__class__.objects.order_by('-position')[0]
                self.position = last.position + 1
            except IndexError:
                # First row
                self.position = 0

        self.sprite, created = Sprite.objects.get_or_create(name='special_effects')
        super(SpecialEffects, self).save(*args, **kwargs)


@receiver(post_delete, sender=SpecialEffects)
def special_effects(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.imgfile:
        instance.imgfile.delete(False)
    if instance.thumbnail:
        instance.thumbnail.delete(False)
