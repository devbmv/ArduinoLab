from django.contrib import admin
from .models import Category, Product, Manufacturer, MicrocontrollerFamily, MicrocontrollerSubfamily, Microcontroller, Peripheral, MicrocontrollerPeripheral, Features

# Admin class for Manufacturer
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')

# Admin class for Product
class ProductAdmin(admin.ModelAdmin):
    # 'price' și 'sku' au fost eliminate pentru că nu există în modelul Product actual.
    list_display = ('name',)

# Admin class for Category
class CategoryAdmin(admin.ModelAdmin):
    # 'friendly_name' a fost eliminat deoarece nu există în modelul Category actualizat.
    list_display = ('name',)

# Admin class for Microcontroller Family
class MicrocontrollerFamilyAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer')

# Admin class for Microcontroller Subfamily
class MicrocontrollerSubfamilyAdmin(admin.ModelAdmin):
    list_display = ('name', 'family')

# Admin class for Microcontroller
class MicrocontrollerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'bit_width',
        'cpu_architecture',
        'max_frequency_mhz',
        'ram_kb',
        'flash_memory_kb',
        'power_consumption_mw',
        'package_type'
    )
    ordering = ('name',)

# Admin class for Peripheral
class PeripheralAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

# Admin class for Microcontroller-Peripheral association
class MicrocontrollerPeripheralAdmin(admin.ModelAdmin):
    list_display = ('microcontroller', 'peripheral', 'quantity')

# Admin class for Features
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('microcontroller', 'has_eeprom', 'has_adc', 'has_dac', 'pwm_pins')

# Registering the models with specific ModelAdmin classes
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(MicrocontrollerFamily, MicrocontrollerFamilyAdmin)
admin.site.register(MicrocontrollerSubfamily, MicrocontrollerSubfamilyAdmin)
admin.site.register(Microcontroller, MicrocontrollerAdmin)
admin.site.register(Peripheral, PeripheralAdmin)
admin.site.register(MicrocontrollerPeripheral, MicrocontrollerPeripheralAdmin)
admin.site.register(Features, FeaturesAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
