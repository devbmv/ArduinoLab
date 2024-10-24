from django.contrib import admin
from .models import Family, Microcontroller


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
    search_fields = ('name', 'cpu_architecture')  # Permite căutarea după nume și arhitectură CPU
    list_filter = ('category', 'bit_width', 'package_type')  # Filtre laterale după familie, lățimea de biți și tipul de pachet
    list_editable = ('bit_width', 'max_frequency_mhz')  # Permite editarea acestor câmpuri direct din listă


class FamilyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    ordering = ('name',)
    search_fields = ('name',)  # Permite căutarea după nume


admin.site.register(Microcontroller, MicrocontrollerAdmin)
admin.site.register(Family, FamilyAdmin)
