# Generated by Django 5.1.2 on 2024-10-20 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_manufacturer_microcontroller_peripheral_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='friendly_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='features',
            name='has_adc',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='features',
            name='has_dac',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='features',
            name='has_eeprom',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='features',
            name='microcontroller',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='features', to='products.microcontroller'),
        ),
        migrations.AlterField(
            model_name='features',
            name='pwm_pins',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='microcontroller',
            name='bit_width',
            field=models.PositiveIntegerField(blank=True, choices=[(8, '8-bit'), (16, '16-bit'), (32, '32-bit')], null=True),
        ),
        migrations.AlterField(
            model_name='microcontroller',
            name='cpu_architecture',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='microcontroller',
            name='flash_memory_kb',
            field=models.PositiveIntegerField(blank=True, help_text='Flash memory capacity in KB', null=True),
        ),
        migrations.AlterField(
            model_name='microcontroller',
            name='max_frequency_mhz',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='microcontroller',
            name='model_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='microcontroller',
            name='package_type',
            field=models.CharField(blank=True, choices=[('DIP', 'DIP'), ('QFP', 'QFP'), ('BGA', 'BGA'), ('TSSOP', 'TSSOP')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='microcontroller',
            name='power_consumption_mw',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Power consumption in milliwatts', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='microcontroller',
            name='ram_kb',
            field=models.PositiveIntegerField(blank=True, help_text='RAM capacity in KB', null=True),
        ),
        migrations.AlterField(
            model_name='microcontroller',
            name='subfamily',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='microcontrollers', to='products.microcontrollersubfamily'),
        ),
        migrations.AlterField(
            model_name='microcontrollerfamily',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='families', to='products.manufacturer'),
        ),
        migrations.AlterField(
            model_name='microcontrollerfamily',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='microcontrollerperipheral',
            name='microcontroller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.microcontroller'),
        ),
        migrations.AlterField(
            model_name='microcontrollerperipheral',
            name='peripheral',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.peripheral'),
        ),
        migrations.AlterField(
            model_name='microcontrollerperipheral',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='microcontrollersubfamily',
            name='family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subfamilies', to='products.microcontrollerfamily'),
        ),
        migrations.AlterField(
            model_name='microcontrollersubfamily',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='peripheral',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
