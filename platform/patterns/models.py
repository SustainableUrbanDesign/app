from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from wagtail.images.models import Image


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
        InlinePanel("gallery_images", label="Gallery images"),
    ]

    parent_page_types = ["patterns.UrbanDesignPatternIndex"]
    subpage_types = []


class UrbanDesignPatternImage(Orderable):
    design_pattern = ParentalKey(
        UrbanDesignPattern, on_delete=models.CASCADE, related_name="gallery_images"
    )
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="design_patterns"
    )
    alt = models.CharField(
        help_text="Alternative text for accessibility.", max_length=250
    )

    panels = [
        ImageChooserPanel("image"),
        FieldPanel("alt"),
    ]


class UrbanDesignPatternTagIndex(Page):
    max_count = 1

    parent_page_types = ["patterns.UrbanDesignPatternIndex"]
    subpage_types = []

    def get_context(self, request):
        context = super().get_context(request)

        # Get design patterns matching current tag
        tag = request.GET.get("tag")
        design_patterns = UrbanDesignPattern.objects.filter(tags__name=tag)

        context["design_patterns"] = design_patterns

        return context


class UrbanDesignPatternIndex(Page):
    max_count = 1

    parent_page_types = ["home.HomePage"]
    subpage_types = [
        "patterns.UrbanDesignPatternTagIndex",
        "patterns.UrbanDesignPattern",
    ]

    def get_context(self, request):
        context = super().get_context(request)

        design_patterns = UrbanDesignPattern.objects.all()

        context["design_patterns"] = design_patterns

        return context
