from django.db import models
from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
import os


class BridalPortfolio(models.Model):
    title = models.CharField(max_length=50, null=False, blank=True)
    imgfile = models.ImageField(upload_to='portfolio/static/img')
    thumbnail = models.ImageField(upload_to='portfolio/static/img', max_length=500, blank=True, null=True)
    position = models.PositiveSmallIntegerField("Position")

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
        THUMBNAIL_SIZE = self.calculateMaxDimensions(self.imgfile.height, self.imgfile.width)

        DJANGO_TYPE = self.imgfile.file.content_type

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

    def calculateMaxDimensions(self, height, width):
        height_to_width_ratio = height / float(width)
        return (120 / height_to_width_ratio, 120)

    def save(self):
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

        super(BridalPortfolio, self).save()
