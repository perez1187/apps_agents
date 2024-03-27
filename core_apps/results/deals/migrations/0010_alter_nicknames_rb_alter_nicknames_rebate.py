# Generated by Django 4.2.7 on 2024-03-25 23:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("deals", "0009_clubs_created_at_clubs_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nicknames",
            name="rb",
            field=models.DecimalField(
                decimal_places=3, default=0.0, max_digits=7, verbose_name="Rakeback"
            ),
        ),
        migrations.AlterField(
            model_name="nicknames",
            name="rebate",
            field=models.DecimalField(
                decimal_places=3, default=0.0, max_digits=7, verbose_name="Rebate"
            ),
        ),
    ]