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
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter SKU'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Microcontroller Name'}),
            'category': forms.Select(attrs={'class': 'form-control'}),

            # Use Select for bit_width as it now has choices
            'bit_width': forms.Select(attrs={'class': 'form-control'}),

            # Use Select for cpu_architecture since it now has defined choices
            'cpu_architecture': forms.Select(attrs={'class': 'form-control'}),

            'max_frequency_mhz': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Max Frequency (MHz)'}),

            # Use Select for RAM size
            'ram_kb': forms.Select(attrs={'class': 'form-control'}),

            # Use Select for Flash memory size
            'flash_memory_kb': forms.Select(attrs={'class': 'form-control'}),

            'power_consumption_mw': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Power Consumption in mW'}),
            'package_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Rating'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Image URL'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Microcontroller name is required.")
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price
