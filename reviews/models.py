from django.db import models


class ClientReview(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, null=True)
    text = models.TextField()
    position = models.PositiveSmallIntegerField("Position")

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        return '%s: written by: %s sample: %s' % ('Displayed' if self.active else 'Hidden', self.name, self.text[:100])

    def save(self):
        if self.position is None:
            # Append
            try:
                last = self.__class__.objects.order_by('-position')[0]
                self.position = last.position + 1
            except IndexError:
                # First row
                self.position = 0

        super(ClientReview, self).save()
