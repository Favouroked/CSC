from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=300, unique=True, default="Title")
    code = models.CharField(max_length=145, unique=True)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.title

class Textbook(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=300)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title