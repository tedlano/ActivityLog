from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=6)
    priority = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class Activity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    link = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject)
    
    class Meta:
        ordering = ['order',]
        
    def __str__(self):
        return self.title