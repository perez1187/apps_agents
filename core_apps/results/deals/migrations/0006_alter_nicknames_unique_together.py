# Generated by Django 4.2.7 on 2024-03-16 12:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("deals", "0005_nicknames_agents_alter_nicknames_nickname_id"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="nicknames",
            unique_together={("agent", "nickname", "nickname_id", "club")},
        ),
    ]
