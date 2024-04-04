from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "view_apps.agents_deals"
    verbose_name = _("Agent Deal")

