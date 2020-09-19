from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel

# TODO: determine if/how to make Client App Settings model a singleton
# Note: this may cause problems with Wagtail multi-site
@register_setting
class ClientAppSettings(BaseSetting):
    url = models.URLField(help_text="Enter URL for the JavaScript client.")

    panels = [FieldPanel("url")]

    class Meta:
        verbose_name = "Client app"

