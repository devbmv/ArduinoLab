# Generated by Django 5.1.2 on 2024-10-20 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_microcontroller_rating_alter_microcontroller_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='microcontroller',
            old_name='model_name',
            new_name='name',
        ),
    ]