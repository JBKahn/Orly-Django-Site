from core.models import Portfolio
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver


class BridalPortfolio(Portfolio):
    class Meta:
        ordering = ['position']

    def get_thumbnail_sprite(self):
        return 'bridal_portfolio'


@receiver(post_delete, sender=BridalPortfolio)
def delete_images(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.imgfile:
        instance.imgfile.delete(False)
    if instance.thumbnail:
        instance.thumbnail.delete(False)
