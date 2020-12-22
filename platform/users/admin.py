from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from .models import User, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    fields = ("user", "given_name", "family_name", "job_title")


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("username", "password1", "password2"),},
        ),
    )
    list_display = ("username", "email", "is_staff")
    search_fields = ("username", "email")


admin.site.register(User, CustomUserAdmin)
