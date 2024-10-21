from django import forms
from .models import Microcontroller, Peripheral, Manufacturer, Features

from django import forms
from .models import Microcontroller


class MicrocontrollerForm(forms.ModelForm):
    class Meta:
        model = Microcontroller
        fields = [
            'sku',
            'name',
            'category',
            'bit_width',
            'cpu_architecture',
            'max_frequency_mhz',
            'ram_kb',
            'flash_memory_kb',
            'power_consumption_mw',
            'package_type',
            'description',
            'price',
            'rating',
            'image_url',
            'image'
        ]
        widgets = {
            # Corrected from 'skyu' to 'sku'
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'bit_width': forms.Select(attrs={'class': 'form-control'}),
            'cpu_architecture': forms.TextInput(attrs={'class': 'form-control'}),
            'max_frequency_mhz': forms.NumberInput(attrs={'class': 'form-control'}),
            'ram_kb': forms.NumberInput(attrs={'class': 'form-control'}),
            'flash_memory_kb': forms.NumberInput(attrs={'class': 'form-control'}),
            'power_consumption_mw': forms.NumberInput(attrs={'class': 'form-control'}),
            'package_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            # Corrected to URLInput
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
            # Corrected to FileInput
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


# Form for Peripheral Model
class PeripheralForm(forms.ModelForm):
    class Meta:
        model = Peripheral
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

# Form for Manufacturer Model


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'website']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
        }

# Form for Features Model


class FeaturesForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = ['has_eeprom', 'has_adc', 'has_dac', 'pwm_pins']
        widgets = {
            'has_eeprom': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_adc': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_dac': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pwm_pins': forms.NumberInput(attrs={'class': 'form-control'}),
        }
