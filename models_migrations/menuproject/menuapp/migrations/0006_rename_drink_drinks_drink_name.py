# Generated by Django 5.1 on 2024-09-01 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menuapp", "0005_drinks"),
    ]

    operations = [
        migrations.RenameField(
            model_name="drinks",
            old_name="drink",
            new_name="drink_name",
        ),
    ]
