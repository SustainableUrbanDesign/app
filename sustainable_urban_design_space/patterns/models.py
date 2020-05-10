from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.search import index


class UrbanDesignPatternTag(TaggedItemBase):
    content_object = ParentalKey(
        "UrbanDesignPattern", on_delete=models.CASCADE, related_name="tagged_items",
    )


class UrbanDesignPattern(Page):
    description = RichTextField()
    tags = ClusterTaggableManager(through=UrbanDesignPatternTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField("description"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("description", classname="full"),
        FieldPanel("tags"),
    ]
