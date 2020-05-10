from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.search import index


class UrbanDesignPattern(Page):
    description = RichTextField()

    search_fields = Page.search_fields + [
        index.SearchField("description"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("description", classname="full"),
    ]
