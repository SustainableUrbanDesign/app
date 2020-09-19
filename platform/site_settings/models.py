from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel


@register_setting
class ClientAppSettings(BaseSetting):
    url = models.URLField(help_text="Enter URL for the JavaScript client.")

    panels = [FieldPanel("url")]

