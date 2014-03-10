from django.db import models
from django.core.mail import send_mail
from django.conf import settings

from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver

from core.models import Thumbnail


class ClientReview(Thumbnail):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, null=True)
    text = models.TextField()

    def __unicode__(self):
        return '%s: written by: %s sample: %s' % ('Displayed' if self.active else 'Hidden', self.name, self.text[:100])

    def get_thumbnail_sprite(self):
        return 'reviews'

    def send_email(self):
        send_mail(
            subject='Website New Review',
            message=self.format_email(),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['josephbkahn@gmail.com'],
            fail_silently=False
        )

    def format_email(self):
       return "Name: {name}\nReview: {review}".format(name=self.name, review=self.text)


@receiver(post_delete, sender=ClientReview)
def delete_images(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.thumbnail:
        instance.thumbnail.delete(False)
