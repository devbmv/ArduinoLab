from .models import StoreSettings, PaymentSettings, ShippingSettings
from django.conf import settings

def global_store_settings(request):
    store_settings = StoreSettings.objects.first() 
    payment_settings = PaymentSettings.objects.first() 
    shipping_settings = ShippingSettings.objects.first() 
    return {
        'store_settings': store_settings,
        'payment_settings': payment_settings,
        'shipping_settings': shipping_settings,
    }
def get_store_settings():
    """Return the first instance of StoreSettings."""
    return StoreSettings.objects.first()

def get_payment_settings():
    """Return the first instance of PaymentSettings."""
    return PaymentSettings.objects.first()

def get_shipping_settings():
    """Return the first instance of ShippingSettings."""
    return ShippingSettings.objects.first()
