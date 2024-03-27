from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.scripts.result_scripts"
    verbose_name = _("Result Script")

