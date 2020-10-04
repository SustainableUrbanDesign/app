from django.db import models


class UrbanDesignPattern(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    # TODO: add tagging
