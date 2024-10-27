from django.contrib import admin
from .models import Family, Microcontroller


class MicrocontrollerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "bit_width",
        "cpu_architecture",
        "max_frequency_mhz",
        "ram_kb",
        "flash_memory_kb",
        "power_consumption_mw",
        "package_type",
    )
    ordering = ("name",)
    search_fields = ("name", "cpu_architecture")
    list_filter = ("category", "bit_width", "package_type")
    list_editable = ("bit_width", "max_frequency_mhz")


class FamilyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)
    search_fields = ("name",)


# Register models with the admin site
admin.site.register(Microcontroller, MicrocontrollerAdmin)
admin.site.register(Family, FamilyAdmin)
