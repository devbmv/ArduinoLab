from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import StoreSettings, PaymentSettings, ShippingSettings, UserSettings
from .forms import StoreSettingsForm, PaymentSettingsForm, ShippingSettingsForm, UserSettingsForm

@login_required
def settings_view(request):
    """ A view to return and update the settings page for superusers """

    # Ensure store settings exist or create new one
    store_settings, _ = StoreSettings.objects.get_or_create(id=1)  # Assuming there's always a single StoreSettings

    # Ensure payment and shipping settings are linked to store settings
    payment_settings, _ = PaymentSettings.objects.get_or_create(store=store_settings)
    shipping_settings, _ = ShippingSettings.objects.get_or_create(store=store_settings)

    # Get the user's settings, or create them if they don't exist
    user_settings, _ = UserSettings.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Bind POST data to the forms
        store_form = StoreSettingsForm(request.POST, instance=store_settings)
        payment_form = PaymentSettingsForm(request.POST, instance=payment_settings)
        shipping_form = ShippingSettingsForm(request.POST, instance=shipping_settings)
        user_settings_form = UserSettingsForm(request.POST, instance=user_settings)

        # Validate all forms
        if store_form.is_valid() and payment_form.is_valid() and shipping_form.is_valid() and user_settings_form.is_valid():
            # Save store settings
            store_form.save()

            # Ensure the store is linked to payment and shipping settings
            payment_settings = payment_form.save(commit=False)
            payment_settings.store = store_settings
            payment_settings.save()

            shipping_settings = shipping_form.save(commit=False)
            shipping_settings.store = store_settings
            shipping_settings.save()

            # Save user settings
            user_settings_form.save()

            # Show success message
            messages.success(request, 'Settings updated successfully!')
            return redirect('home')  # Redirect back to the home page after saving
        else:
            # If any forms are invalid, display error message
            messages.error(request, 'Please correct the errors in the forms.')
    else:
        # Initialize forms with current instance data
        store_form = StoreSettingsForm(instance=store_settings)
        payment_form = PaymentSettingsForm(instance=payment_settings)
        shipping_form = ShippingSettingsForm(instance=shipping_settings)
        user_settings_form = UserSettingsForm(instance=user_settings)

    # Pass forms to template context
    context = {
        'store_form': store_form,
        'payment_form': payment_form,
        'shipping_form': shipping_form,
        'user_settings_form': user_settings_form,  # Include user settings form in the context
    }

    return render(request, 'store_settings/settings.html', context)


def change_password(request):
    """ A view to change the user's password """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevent user from being logged out
            messages.success(request, 'Password changed successfully!')
            return redirect('settings')  # Redirect back to the home page after changing password
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'store_settings/change_password.html', {'form': form})
