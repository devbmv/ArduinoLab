# Generated by Django 5.1.2 on 2024-10-25 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0014_alter_microcontroller_bit_width_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="microcontroller",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="microcontroller",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
