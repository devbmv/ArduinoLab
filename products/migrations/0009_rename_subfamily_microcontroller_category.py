# Generated by Django 5.1.2 on 2024-10-20 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_microcontroller_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='microcontroller',
            old_name='subfamily',
            new_name='category',
        ),
    ]
