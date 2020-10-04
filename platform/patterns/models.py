from django.db import models

from taggit.managers import TaggableManager


class UrbanDesignPattern(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = TaggableManager()
    image = models.ImageField()
