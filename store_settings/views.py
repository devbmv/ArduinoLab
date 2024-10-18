from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import StoreSettings, PaymentSettings, ShippingSettings
from .forms import StoreSettingsForm, PaymentSettingsForm, ShippingSettingsForm

@user_passes_test(lambda u: u.is_superuser)
def settings_view(request):
    """ A view to return and update the settings page for superusers """

    # Get the existing store settings from the database
    store_settings = StoreSettings.objects.first()  # Assuming there's only one StoreSettings object
    
    if store_settings is None:
        # Handle the case where store_settings is not found
        return redirect('create_store_settings')  # Redirect to a page where store settings can be created
    
    # Get related payment and shipping settings based on the store
    payment_settings = PaymentSettings.objects.filter(store=store_settings).first()
    shipping_settings = ShippingSettings.objects.filter(store=store_settings).first()

    # Initialize forms with existing data
    if request.method == 'POST':
        store_form = StoreSettingsForm(request.POST, instance=store_settings)
        payment_form = PaymentSettingsForm(request.POST, instance=payment_settings)
        shipping_form = ShippingSettingsForm(request.POST, instance=shipping_settings)

        # Validate all forms
        if store_form.is_valid() and payment_form.is_valid() and shipping_form.is_valid():
            # Save the store settings form
            store_form.save()

            # Set the store for payment and shipping settings before saving
            payment_settings = payment_form.save(commit=False)
            payment_settings.store = store_settings  # Ensure the store is set
            payment_settings.save()

            shipping_settings = shipping_form.save(commit=False)
            shipping_settings.store = store_settings  # Ensure the store is set
            shipping_settings.save()

            return redirect('settings')  # Redirect back to the settings page after saving
    else:
        # Create form instances with the current settings data
        store_form = StoreSettingsForm(instance=store_settings)
        payment_form = PaymentSettingsForm(instance=payment_settings)
        shipping_form = ShippingSettingsForm(instance=shipping_settings)

    # Send the forms to the template
    context = {
        'store_form': store_form,
        'payment_form': payment_form,
        'shipping_form': shipping_form,
    }

    return render(request, 'store_settings/settings.html', context)
