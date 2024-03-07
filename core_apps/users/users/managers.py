from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):


    def create_user(
        self, username, password, **extra_fields
    ):
        if not username:
            raise ValueError(_("Users must submit a username"))

        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_agent", False)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, password, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_agent", False)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is_superuser=True"))
        if not password:
            raise ValueError(_("Superusers must have a password"))

        user = self.create_user(
            username, password, **extra_fields
        )
        user.save(using=self._db)
        return user