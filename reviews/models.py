from django.db import models
from django.core.mail import send_mail
from django.conf import settings


class ClientReview(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, null=True)
    text = models.TextField()
    position = models.PositiveSmallIntegerField("Position")

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        return '%s: written by: %s sample: %s' % ('Displayed' if self.active else 'Hidden', self.name, self.text[:100])

    def save(self, **kwargs):
        if self.position is None:
            # Append
            try:
                last = self.__class__.objects.order_by('-position')[0]
                self.position = last.position + 1
            except IndexError:
                # First row
                self.position = 0

            self.send_email()

        super(ClientReview, self).save()

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
