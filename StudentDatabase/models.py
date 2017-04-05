from __future__ import unicode_literals
from django.db import models

## Creation of the Django database
class Student(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    ColourFilter = models.BooleanField()
    SoundFilter= models.BooleanField()

    def __str__(self):
        return self.name