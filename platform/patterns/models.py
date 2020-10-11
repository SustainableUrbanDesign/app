from django.db import models

from taggit.managers import TaggableManager


class UrbanDesignPattern(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    keywords = TaggableManager(blank=True, verbose_name="Keywords", help_text="A comma-separated list of keywords.")
