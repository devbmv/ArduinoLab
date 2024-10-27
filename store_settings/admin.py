from django.contrib import admin
from .models import StoreSettings, PaymentSettings, ShippingSettings, UserSettings


class StoreSettingsAdmin(admin.ModelAdmin):
    list_display = ("store_name", "contact_email", "currency")
    search_fields = ("store_name", "contact_email")
    list_editable = ("currency",)
    list_filter = ("currency",)


class PaymentSettingsAdmin(admin.ModelAdmin):
    list_display = ("store", "stripe_public_key", "paypal_client_id")
    search_fields = ("store__store_name",)
    list_filter = ("store",)


class ShippingSettingsAdmin(admin.ModelAdmin):
    list_display = ("store", "standard_shipping_cost", "free_shipping_threshold")
    search_fields = ("store__store_name",)
    list_editable = ("standard_shipping_cost", "free_shipping_threshold")


class UserSettingsAdmin(admin.ModelAdmin):
    list_display = ("user", "preferred_language", "receive_newsletter")
    search_fields = ("user__username", "user__email")
    list_editable = ("preferred_language", "receive_newsletter")
    list_filter = ("preferred_language", "receive_newsletter")


# Înregistrăm modelele în admin
admin.site.register(StoreSettings, StoreSettingsAdmin)
admin.site.register(PaymentSettings, PaymentSettingsAdmin)
admin.site.register(ShippingSettings, ShippingSettingsAdmin)
admin.site.register(UserSettings, UserSettingsAdmin)
