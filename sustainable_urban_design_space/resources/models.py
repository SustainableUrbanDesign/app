from django.core.validators import int_list_validator, MinLengthValidator
from django.db import models

from wagtail.core.models import Page


class Book(Page):
    isbn = models.CharField(
        max_length=13, validators=[int_list_validator(sep="-"), MinLengthValidator(9),],
    )
