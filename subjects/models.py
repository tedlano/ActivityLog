from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=6)
    priority = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title