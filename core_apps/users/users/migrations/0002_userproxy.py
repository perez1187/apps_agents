# Generated by Django 4.2.7 on 2024-03-26 15:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProxy",
            fields=[],
            options={
                "verbose_name": "Result by User",
                "verbose_name_plural": "Results by Users",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("users.user",),
        ),
    ]