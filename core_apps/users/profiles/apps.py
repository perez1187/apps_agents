from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.users.profiles"
    verbose_name = _("Profiles")

    def ready(self):
        from core_apps.users.profiles import signals    