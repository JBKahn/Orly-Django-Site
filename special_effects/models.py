from core.models import Portfolio
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver


class SpecialEffects(Portfolio):
    class Meta:
        ordering = ['position']

    def get_thumbnail_sprite(self):
        return 'special_effects'


@receiver(post_delete, sender=SpecialEffects)
def delete_images(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.imgfile:
        instance.imgfile.delete(False)
    if instance.thumbnail:
        instance.thumbnail.delete(False)
