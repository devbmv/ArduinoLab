# Generated by Django 5.1.2 on 2024-10-24 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0011_microcontroller_image_url"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Category",
        ),
        migrations.DeleteModel(
            name="Product",
        ),
    ]
