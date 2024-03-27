from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.scripts.user_scripts"
    verbose_name = _("User Script")

