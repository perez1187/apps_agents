# Generated by Django 4.2.7 on 2024-03-16 11:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("deals", "0002_alter_nicknames_player"),
    ]

    operations = [
        migrations.AddField(
            model_name="nicknames",
            name="nickname_id",
            field=models.CharField(
                blank=True, max_length=40, null=True, verbose_name="Nickname"
            ),
        ),
    ]
