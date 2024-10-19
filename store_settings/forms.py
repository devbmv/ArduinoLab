from django import forms
from .models import StoreSettings, PaymentSettings, ShippingSettings, UserSettings

class StoreSettingsForm(forms.ModelForm):
    """Form for updating store settings"""
    class Meta:
        model = StoreSettings
        fields = ['store_name', 'store_description', 'contact_email', 'currency']

class PaymentSettingsForm(forms.ModelForm):
    """Form for updating payment settings"""
    class Meta:
        model = PaymentSettings
        fields = ['stripe_public_key', 'stripe_secret_key', 'paypal_client_id', 'paypal_client_secret']

class ShippingSettingsForm(forms.ModelForm):
    """Form for updating shipping settings"""
    class Meta:
        model = ShippingSettings
        fields = ['standard_shipping_cost', 'free_shipping_threshold']

class UserSettingsForm(forms.ModelForm):
    """Form for updating user-specific settings"""
    class Meta:
        model = UserSettings
        fields = ['preferred_language', 'receive_newsletter']
