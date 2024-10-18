from django.contrib import admin
from .models import ShippingSettings, PaymentSettings, StoreSettings



admin.site.register(ShippingSettings)

admin.site.register(PaymentSettings)

admin.site.register(StoreSettings)

