# Generated by Django 5.1.2 on 2024-10-20 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_category_friendly_name_remove_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='microcontroller',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]