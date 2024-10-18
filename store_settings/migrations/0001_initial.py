# Generated by Django 5.1.2 on 2024-10-18 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(help_text='Name of the store', max_length=255)),
                ('store_description', models.TextField(help_text='Short description of the store')),
                ('contact_email', models.EmailField(help_text='Email for customer support', max_length=254)),
                ('currency', models.CharField(default='EUR', help_text='Currency used in the store', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_shipping_cost', models.DecimalField(decimal_places=2, default=5.0, help_text='Standard shipping cost', max_digits=6)),
                ('free_shipping_threshold', models.DecimalField(decimal_places=2, default=50.0, help_text='Free shipping for orders above this value', max_digits=6)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_settings', to='store_settings.storesettings')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_public_key', models.CharField(blank=True, help_text='Stripe public API key', max_length=255)),
                ('stripe_secret_key', models.CharField(blank=True, help_text='Stripe secret API key', max_length=255)),
                ('paypal_client_id', models.CharField(blank=True, help_text='PayPal client ID', max_length=255)),
                ('paypal_client_secret', models.CharField(blank=True, help_text='PayPal secret key', max_length=255)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_settings', to='store_settings.storesettings')),
            ],
        ),
    ]
