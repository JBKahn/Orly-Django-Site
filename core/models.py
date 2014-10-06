import os

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models

from cStringIO import StringIO
from PIL import Image

from mysite.settings import STATICFILES_DIRS


class Sprite(models.Model):
    image = models.ImageField(upload_to=STATICFILES_DIRS[0] + '/img', null=True, blank=True)
    name = models.CharField(max_length=50, null=False, blank=False)

    def __unicode__(self):
        return self.name

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
            total_height += (sprite.thumbnail or 0) and sprite.thumbnail.height

        img_sprite = Image.new("RGBA", (233, total_height))
        height_offset = 0

        for portfolio_object in spriteitems:

            if not portfolio_object.thumbnail:
                continue
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

    def get_sprite_data(self):
        spriteitems = []
        if self.bridalportfolio_set.exists():
            spriteitems = self.bridalportfolio_set.order_by('position')
            return [
                {
                    "big_path": ('/').join(piece.imgfile.name.split('/')[-2:]),
                    "small_path": ('/').join(self.image.path.split('/')[-2:]),
                    "title": piece.title or ' ',
                    "thumbnail_height": piece.thumbnail.height,
                    "thumbnail_width": piece.thumbnail.width,
                    "thumbnail_offset_top": piece.thumbnail_sprite_offset_top - piece.thumbnail.height
                } for piece in spriteitems
            ]
        elif self.specialeffects_set.exists():
            spriteitems = self.specialeffects_set.order_by('position')
            return [
                {
                    "big_path": ('/').join(piece.imgfile.name.split('/')[-2:]),
                    "small_path": ('/').join(self.image.path.split('/')[-2:]),
                    "title": piece.title or ' ',
                    "thumbnail_height": piece.thumbnail.height,
                    "thumbnail_width": piece.thumbnail.width,
                    "thumbnail_offset_top": piece.thumbnail_sprite_offset_top - piece.thumbnail.height
                } for piece in spriteitems
            ]
        elif self.clientreview_set.exists():
            spriteitems = self.clientreview_set.order_by('position')
            items = []
            for piece in spriteitems:
                items.append(
                    {
                        "thumbnail_path": (self.image or None) and ('/').join(self.image.path.split('/')[-2:]),
                        "text": piece.text,
                        "author": piece.name,
                        "thumbnail_height": (piece.thumbnail or None) and piece.thumbnail.height,
                        "thumbnail_width": (piece.thumbnail or None) and piece.thumbnail.width,
                        "thumbnail_offset_top": (piece.thumbnail or None) and piece.thumbnail_sprite_offset_top - piece.thumbnail.height
                    }
                )
            return items
        return []


class Thumbnail(models.Model):
    thumbnail = models.ImageField(upload_to=STATICFILES_DIRS[0] + '/img', max_length=500, blank=True, null=True)
    position = models.PositiveSmallIntegerField("Position")
    thumbnail_sprite_offset_top = models.PositiveSmallIntegerField(default=0)
    sprite = models.ForeignKey(Sprite)

    class Meta:
        ordering = ['position']
        abstract = True

    def get_thumbnail_sprite(self):
        return ''

    def format_thumbnail(self):
        return u'<img src="{}" />'.format(static('img/' + self.thumbnail.url.split('/')[-1]))
    format_thumbnail.allow_tags = True

    def resize_thumbnail(self):
        # original code for this method came from
        # http://snipt.net/danfreak/generate-thumbnails-in-django-with-pil/

        # If there is no image associated with this.
        # do not create thumbnail
        if not self.thumbnail:
            return

        if self.thumbnail.height == 100 and self.thumbnail.width == 100:
            return

        # Set our max thumbnail size in a tuple (max width, max height)
        THUMBNAIL_SIZE = (100, 100)

        if hasattr(self.thumbnail.file, 'content_type'):
            DJANGO_TYPE = self.thumbnail.file.content_type
        else:
            if self.thumbnail.file.name[-3:] == 'png':
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
        self.thumbnail.file.open()
        image = Image.open(self.thumbnail.file)

        # Use Image.ANTIALIAS to reduce potential artifacts that may result
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
        image.crop((0, 0, 150, 150))

        # Save the thumbnail
        temp_handle = StringIO()
        image.save(temp_handle, PIL_TYPE)
        self.thumbnail.file.close()
        temp_handle.seek(0)

        suf = SimpleUploadedFile(os.path.split(self.thumbnail.name)[-1], temp_handle.read(), content_type=DJANGO_TYPE)
        self.thumbnail.save('%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENSION), suf, save=False)

    def save(self, *args, **kwargs):
        if self.get_thumbnail_sprite() == 'reviews':
            self.resize_thumbnail()
        if self.position is None:
            # Append
            try:
                last = self.__class__.objects.order_by('-position')[0]
                self.position = last.position + 1
            except IndexError:
                # First row
                self.position = 0

        self.sprite, created = Sprite.objects.get_or_create(name=self.get_thumbnail_sprite())

        super(Thumbnail, self).save(*args, **kwargs)


class Portfolio(Thumbnail):
    title = models.CharField(max_length=50, null=True, blank=True)
    imgfile = models.ImageField(upload_to=STATICFILES_DIRS[0] + '/img')

    class Meta:
        abstract = True

    def create_thumbnail_from_image(self):
        # original code for this method came from
        # http://snipt.net/danfreak/generate-thumbnails-in-django-with-pil/

        # If there is no image associated with this.
        # do not create thumbnail
        if not self.imgfile:
            return

        # Set our max thumbnail size in a tuple (max width, max height)
        THUMBNAIL_SIZE = (223, 1000000)

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
            self.create_thumbnail_from_image()
        if self.position is None:
            # Append
            try:
                last = self.__class__.objects.order_by('-position')[0]
                self.position = last.position + 1
            except IndexError:
                # First row
                self.position = 0

        self.sprite, created = Sprite.objects.get_or_create(name=self.get_thumbnail_sprite())

        super(Portfolio, self).save(*args, **kwargs)
