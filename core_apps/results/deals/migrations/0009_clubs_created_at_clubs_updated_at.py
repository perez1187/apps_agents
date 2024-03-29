# Generated by Django 4.2.7 on 2024-03-25 00:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("deals", "0008_clubs"),
    ]

    operations = [
        migrations.AddField(
            model_name="clubs",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="clubs",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
