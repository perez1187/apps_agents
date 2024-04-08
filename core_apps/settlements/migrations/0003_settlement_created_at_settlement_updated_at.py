# Generated by Django 4.2.7 on 2024-04-06 21:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("settlements", "0002_settlement_agent_alter_settlement_player"),
    ]

    operations = [
        migrations.AddField(
            model_name="settlement",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="settlement",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
