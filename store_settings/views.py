from .models import UserSettings  # Asigură-te că ai modelul UserSettings
from django.contrib.messages import get_messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import UserSettings
from .forms import NewsletterForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import StoreSettings, PaymentSettings, ShippingSettings, UserSettings
from .forms import (
    StoreSettingsForm,
    PaymentSettingsForm,
    ShippingSettingsForm,
    UserSettingsForm,
)


@login_required
def settings_view(request):
    """A view to return and update the settings page for superusers."""

    # Ensure store settings exist or create new one
    store_settings, _ = StoreSettings.objects.get_or_create(
        id=1
    )  # Assuming there's always a single StoreSettings

    # Ensure payment and shipping settings are linked to store settings
    payment_settings, _ = PaymentSettings.objects.get_or_create(store=store_settings)
    shipping_settings, _ = ShippingSettings.objects.get_or_create(store=store_settings)

    # Get the user's settings, or create them if they don't exist
    user_settings, _ = UserSettings.objects.get_or_create(user=request.user)

    if request.method == "POST":
        # Bind POST data to the forms
        store_form = StoreSettingsForm(request.POST, instance=store_settings)
        payment_form = PaymentSettingsForm(request.POST, instance=payment_settings)
        shipping_form = ShippingSettingsForm(request.POST, instance=shipping_settings)
        user_settings_form = UserSettingsForm(request.POST, instance=user_settings)

        # Validate all forms
        if (
            store_form.is_valid()
            and payment_form.is_valid()
            and shipping_form.is_valid()
            and user_settings_form.is_valid()
        ):
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
            messages.success(request, "Settings updated successfully!")
            # Redirect back to the home page after saving
            return redirect("home")
        else:
            # If any forms are invalid, display error message
            messages.error(request, "Please correct the errors in the forms.")
    else:
        # Initialize forms with current instance data
        store_form = StoreSettingsForm(instance=store_settings)
        payment_form = PaymentSettingsForm(instance=payment_settings)
        shipping_form = ShippingSettingsForm(instance=shipping_settings)
        user_settings_form = UserSettingsForm(instance=user_settings)

    # Pass forms to template context
    context = {
        "store_form": store_form,
        "payment_form": payment_form,
        "shipping_form": shipping_form,
        # Include user settings form in the context
        "user_settings_form": user_settings_form,
    }

    return render(request, "store_settings/settings.html", context)


def change_password(request):
    """A view to change the user's password."""
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Prevent user from being logged out
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully!")
            # Redirect back to the home page after changing password
            return redirect("settings")
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "store_settings/change_password.html", {"form": form})


# store_settings/views.py


@login_required
def toggle_newsletter(request):
    """Permite utilizatorilor să se aboneze sau să se dezaboneze de la
    newsletter."""
    if request.method == "POST":
        # Obține sau creează setările utilizatorului
        user_settings, created = UserSettings.objects.get_or_create(user=request.user)

        # Toggle pentru starea abonamentului
        user_settings.receive_newsletter = not user_settings.receive_newsletter
        user_settings.save()

        # Mesaj în funcție de noua stare
        if user_settings.receive_newsletter:
            messages.success(
                request, "You have successfully subscribed to the newsletter."
            )
        else:
            messages.info(
                request, "You have successfully unsubscribed from the newsletter."
            )

        return JsonResponse(
            {"status": "success", "subscribed": user_settings.receive_newsletter}
        )

    return JsonResponse({"status": "error"}, status=400)
