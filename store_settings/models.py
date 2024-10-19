from django.db import models
from django.contrib.auth.models import User


class StoreSettings(models.Model):

    """ General store settings """
    store_name = models.CharField(max_length=255)
    store_description = models.TextField()
    contact_email = models.EmailField()
    currency = models.CharField(max_length=10, default="EUR")

    def __str__(self):
        return self.store_name


class PaymentSettings(models.Model):
    """ Payment settings related to store """
    store = models.ForeignKey(StoreSettings, on_delete=models.CASCADE, related_name='payment_settings')
    stripe_public_key = models.CharField( max_length=255, blank=True)
    stripe_secret_key = models.CharField( max_length=255, blank=True)
    paypal_client_id = models.CharField(max_length=255, blank=True)
    paypal_client_secret = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Payment settings for {self.store.store_name}"


class ShippingSettings(models.Model):
    """ Shipping settings related to store """
    store = models.ForeignKey(
        StoreSettings, on_delete=models.CASCADE, related_name='shipping_settings')
    standard_shipping_cost = models.DecimalField(
        max_digits=6, decimal_places=2, default=5.00)
    free_shipping_threshold = models.DecimalField(
        max_digits=6, decimal_places=2, default=50.00)

    def __str__(self):
        return f"Shipping settings for {self.store.store_name}"


class UserSettings(models.Model):
    """ User-specific settings """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_language = models.CharField(
        max_length=50, default="en")
    receive_newsletter = models.BooleanField(
        default=True)

    def __str__(self):
        return self.user.username
