from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


User = get_user_model()

class Profile(models.Model):

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)

    about_user = models.TextField(
        verbose_name=_("about User"),
        default="user description",
    )

    def __str__(self):
        return f"{self.user.username}'s profile"

