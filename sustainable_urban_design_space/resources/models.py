from django.core.validators import int_list_validator, MinLengthValidator
from django.db import models

from wagtail.core.models import Page


class Book(Page):
    isbn = models.CharField(
        max_length=13, validators=[int_list_validator(sep="-"), MinLengthValidator(9),],
    )


class ResourcesIndex(Page):
    max_count = 1

    parent_page_types = ["home.HomePage"]
    subpage_types = [
        "resources.Book",
    ]

    def get_context(self, request):
        context = super().get_context(request)

        books = Book.objects.all()

        context["books"] = books

        return context
