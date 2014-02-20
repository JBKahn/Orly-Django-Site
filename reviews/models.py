from django.db import models


class ClientReview(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, null=True)
    text = models.TextField()
