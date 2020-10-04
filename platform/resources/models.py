from django.core.validators import int_list_validator, MinLengthValidator
from django.db import models


class Book(models.Model):
    isbn = models.CharField(
        max_length=13,
        validators=[int_list_validator(sep="-"), MinLengthValidator(9),],
        help_text="Enter an ISBN (9, 10, or 13) with optional hyphens.",
    )


class DataSource(models.Model):
    description = models.TextField(null=True)
    link = models.URLField()
