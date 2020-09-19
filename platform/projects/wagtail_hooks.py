from wagtail.contrib.modeladmin.helpers import PageButtonHelper
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from site_settings.models import ClientAppSettings
from .models import Project


class ProjectAdminButtonHelper(PageButtonHelper):
    configure_button_classnames = ["button-small", "icon", "icon-site"]

    def configure_button(self, obj):
        text = "Configure project"
        client_app_settings = ClientAppSettings.objects.get()
        client_app_url = client_app_settings.url

        return {
            # "url": client_app_settings.url,
            "url": client_app_url,
            "label": text,
            "title": text,
            "classname": self.finalise_classname(self.configure_button_classnames),
        }

    def get_buttons_for_obj(
        self, obj, exclude=None, classnames_add=None, classnames_excluded=None
    ):
        buttons = super().get_buttons_for_obj(
            obj, exclude, classnames_add, classnames_excluded
        )

        buttons.append(self.configure_button(obj))

        return buttons


class ProjectAdmin(ModelAdmin):
    model = Project
    menu_icon = "pilcrow"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title",)
    search_fields = ("title",)

    button_helper_class = ProjectAdminButtonHelper


modeladmin_register(ProjectAdmin)
