from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Project


class ProjectAdmin(ModelAdmin):
    model = Project
    menu_icon = "pilcrow"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title",)
    search_fields = ("title",)


modeladmin_register(ProjectAdmin)
