from django import forms
from .models import Microcontroller


class MicrocontrollerForm(forms.ModelForm):
    delete_image = forms.BooleanField(required=False, 
                                      label="Delete existing image")

    class Meta:
        model = Microcontroller
        fields = [
            "sku",
            "name",
            "category",
            "bit_width",
            "cpu_architecture",
            "max_frequency_mhz",
            "ram_kb",
            "flash_memory_kb",
            "power_consumption_mw",
            "package_type",
            "description",
            "price",
            "rating",
            "image_url",
            "image",
            "delete_image",  # adaugă câmpul delete_image în fields
        ]
        widgets = {
            "sku": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter SKU"}
            ),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Microcontroller Name",
                }
            ),
            "category": forms.Select(attrs={"class": "form-control"}),
            # Use Select for bit_width as it now has choices
            "bit_width": forms.Select(attrs={"class": "form-control"}),
            # Use Select for cpu_architecture since it now has defined choices
            "cpu_architecture": forms.Select(attrs={"class": "form-control"}),
            "max_frequency_mhz": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Max Frequency (MHz)",
                }
            ),
            # Use Select for RAM size
            "ram_kb": forms.Select(attrs={"class": "form-control"}),
            # Use Select for Flash memory size
            "flash_memory_kb": forms.Select(attrs={"class": "form-control"}),
            "power_consumption_mw": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Power Consumption in mW",
                }
            ),
            "package_type": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter description",
                    "rows": 3,
                }
            ),
            "price": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter Price"}
            ),
            "rating": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter Rating"}
            ),
            "image_url": forms.URLInput(
                attrs={"class": "form-control",
                        "placeholder": "Enter Image URL"}
            ),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Șterge imaginea dacă delete_image este bifat
        if self.cleaned_data.get("delete_image") and instance.image:
            instance.image.delete()  # Șterge imaginea din stocare
            instance.image = None  # Setează câmpul imaginii pe None

        if commit:
            instance.save()
        return instance

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name:
            raise forms.ValidationError("Microcontroller name is required.")
        return name

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price
