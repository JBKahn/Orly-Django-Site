import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver

from cStringIO import StringIO
from PIL import Image

from mysite.settings import STATIC_URL


class Sprite(models.Model):
    image = models.ImageField(upload_to=STATIC_URL[1:] + 'img', null=True, blank=True)
    name = models.CharField(max_length=50, null=False, blank=False)

    def generate(self):
        spriteitems = []
        if self.bridalportfolio_set.exists():
            spriteitems = self.bridalportfolio_set.order_by('id')
        elif self.specialeffects_set.exists():
            spriteitems = self.specialeffects_set.order_by('id')
        elif self.clientreview_set.exists():
            spriteitems = self.clientreview_set.order_by('id')

        if len(spriteitems) == 0:
            return

        total_height = 0
        for sprite in spriteitems:
            total_height += sprite.thumbnail.height

        img_sprite = Image.new("RGBA", (233, total_height))
        height_offset = 0
        
        for portfolio_object in spriteitems:
            pasteBox = (
                0,  # x cordinate 1
                height_offset,  # y coordinate 1
                portfolio_object.thumbnail.width,  # x cordinate 2
                height_offset + portfolio_object.thumbnail.height  # y cordinate 2
            )
            portfolio_image = Image.open(portfolio_object.thumbnail.path)
            height_offset += portfolio_object.thumbnail.height
            img_sprite.paste(portfolio_image, pasteBox)
            portfolio_object.thumbnail_sprite_offset_top = height_offset
            portfolio_object.save()
            portfolio_image = None

        temp_handle = StringIO()
        img_sprite.save(temp_handle, 'png')
        temp_handle.seek(0)

        suf = SimpleUploadedFile(
            os.path.split(self.name)[-1],
            temp_handle.read(),
            content_type='image/png'
        )
        self.image.delete(False)
        self.image.save(
            '%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], 'png'),
            suf,
            save=False
        )
        self.save()


class BridalPortfolio(models.Model):
    title = models.CharField(max_length=50, null=False, blank=True)
    imgfile = models.ImageField(upload_to=STATIC_URL[1:] + 'img')
    thumbnail = models.ImageField(upload_to=STATIC_URL[1:] + 'img', max_length=500, blank=True, null=True)
    position = models.PositiveSmallIntegerField("Position")
    thumbnail_sprite_offset_top = models.PositiveSmallIntegerField(default=0)
    sprite = models.ForeignKey(Sprite)

    class Meta:
        ordering = ['position']

    def format_thumbnail(self):
        return u'<img src="/%s" />' % '/'.join(self.thumbnail.url.split('/'))
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

        suf = SimpleUploadedFile(
            os.path.split(self.imgfile.name)[-1],
            temp_handle.read(),
            content_type=DJANGO_TYPE
        )
        self.thumbnail.save(
            '%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENSION),
            suf,
            save=False
        )

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

        self.sprite, created = Sprite.objects.get_or_create(name='bridal_portfolio')

        super(BridalPortfolio, self).save(*args, **kwargs)


@receiver(post_delete, sender=BridalPortfolio)
def bridal_portfolio(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.imgfile:
        instance.imgfile.delete(False)
    if instance.thumbnail:
        instance.thumbnail.delete(False)
