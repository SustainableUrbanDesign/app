from django.core.validators import int_list_validator, MinLengthValidator
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page

class Book(Page):
    isbn = models.CharField(
        max_length=13,
        validators=[int_list_validator(sep="-"), MinLengthValidator(9),],
        help_text="Enter an ISBN (9, 10, or 13) with optional hyphens.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("isbn"),
    ]

class DataSource(Page):
    link = models.URLField()

    content_panels = Page.content_panels + [
        FieldPanel("link"),
    ]


class ResourcesIndex(Page):
    max_count = 1

    parent_page_types = ["home.HomePage"]
    subpage_types = [
        "resources.Book",
    ]

    def get_context(self, request):
        context = super().get_context(request)

        context["books"] = Book.objects.all()

        return context
