from __future__ import unicode_literals
from django.db import models

# Create your models here.


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    ColourFilter = models.BooleanField()
    SoundFilter= models.BooleanField()

    def __str__(self):
        return self.name