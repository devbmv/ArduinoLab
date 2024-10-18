from django.db import models

class StoreSettings(models.Model):
    """ General store settings """
    store_name = models.CharField(max_length=255, help_text="Name of the store")
    store_description = models.TextField(help_text="Short description of the store")
    contact_email = models.EmailField(help_text="Email for customer support")
    currency = models.CharField(max_length=10, default="EUR", help_text="Currency used in the store")

    def __str__(self):
        return self.store_name

class PaymentSettings(models.Model):
    """ Payment settings related to store """
    store = models.ForeignKey(StoreSettings, on_delete=models.CASCADE, related_name='payment_settings')
    stripe_public_key = models.CharField(max_length=255, blank=True, help_text="Stripe public API key")
    stripe_secret_key = models.CharField(max_length=255, blank=True, help_text="Stripe secret API key")
    paypal_client_id = models.CharField(max_length=255, blank=True, help_text="PayPal client ID")
    paypal_client_secret = models.CharField(max_length=255, blank=True, help_text="PayPal secret key")

    def __str__(self):
        return f"Payment settings for {self.store.store_name}"


class ShippingSettings(models.Model):
    """ Shipping settings related to store """
    store = models.ForeignKey(StoreSettings, on_delete=models.CASCADE, related_name='shipping_settings')
    standard_shipping_cost = models.DecimalField(max_digits=6, decimal_places=2, default=5.00, help_text="Standard shipping cost")
    free_shipping_threshold = models.DecimalField(max_digits=6, decimal_places=2, default=50.00, help_text="Free shipping for orders above this value")

    def __str__(self):
        return f"Shipping settings for {self.store.store_name}"
