from django.db import models


class BridalPortfolio(models.Model):
    imgfile = models.FileField(upload_to='portfolio/static/img')
