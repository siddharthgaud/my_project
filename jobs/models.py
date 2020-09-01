from django.db import models


# Create your models here.

class Job(models.Model):
    # for image
    image = models.ImageField(upload_to='images/')
    # for details
    summary = models.CharField(max_length=200)
