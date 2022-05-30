from django.db import models

# Create your models here.


class Star(models.Model):
    name = models.CharField(max_length=200)
    classification = models.CharField(max_length=200)
    age = models.BigIntegerField()
