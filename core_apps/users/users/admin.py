from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ["username"]
    model = User
    list_display = [
        "pkid",
        "id",
        "username",
        "is_agent",
        "is_staff",
        "is_active",
    ]
    list_display_links = ["id", "username"]
    list_filter = ["username", "is_staff","is_agent"]
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (
            _("Personal Information"),
            {"fields": ()},
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    'is_agent',
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ["username"]


admin.site.register(User, UserAdmin)