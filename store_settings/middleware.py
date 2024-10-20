from .models import StoreSettings, PaymentSettings, ShippingSettings

class StoreSettingsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.store_settings = StoreSettings.objects.first()
        request.payment_settings = PaymentSettings.objects.first()
        request.shipping_settings = ShippingSettings.objects.first()

        response = self.get_response(request)
        return response
