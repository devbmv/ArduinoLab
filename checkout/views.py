import logging
from django.shortcuts import (render,
                              redirect,
                              reverse,
                              get_object_or_404,
                              HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Microcontroller
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    Cache checkout data in the payment intent metadata.

    This function is used to store additional information in the Stripe
    PaymentIntent metadata before the payment is processed.

    Parameters:
    request (HttpRequest): The HTTP request object containing POST data
                    with the client secret and other checkout information.

    Returns:
    HttpResponse: An HTTP response with status 200 if successful,
      or 400 if an error occurs.
    """
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "bag": json.dumps(request.session.get("bag", {})),
                "save_info": request.POST.get("save_info"),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be processed right now. "
            "Please try again later.",
        )
        return HttpResponse(content=e, status=400)


logger = logging.getLogger(__name__)


def checkout(request):
    """
    Handle the checkout process for a user's order.

    This function manages both the display of the checkout form and the 
    processing of the order when the form is submitted. It interacts with the
    Stripe API to create a payment intent and handles the creation of order
    and order line items in the database.

    Parameters:
    request: The HTTP request object containing POST data for order
    submission or GET data for displaying the checkout form.

    Returns:
    Renders the checkout page with the order form and Stripe client
            secret if the request method is GET. Redirects to the checkout
            success page if the order is successfully processed, or back to
            the bag view if an error occurs.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        bag = request.session.get("bag", {})

        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment.")
            return redirect(reverse("products"))

        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "country": request.POST["country"],
            "postcode": request.POST["postcode"],
            "town_or_city": request.POST["town_or_city"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "county": request.POST["county"],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            try:
                # Create and save the order
                order = order_form.save(commit=False)
                pid = request.POST.get("client_secret").split("_secret")[0]
                order.stripe_pid = pid
                order.original_bag = json.dumps(bag)
                order.save()  # Save order to generate the ID

                logger.info(f"Order created with ID {order.id}")

                for item_id, item_data in bag.items():
                    try:
                        product = Microcontroller.objects.get(id=item_id)

                        if isinstance(item_data, int):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=item_data,
                            )
                        else:
                            for size, quantity in (
                                item_data["items_by_size"].items()
                            ):
                                order_line_item = OrderLineItem(
                                    order=order,
                                    product=product,
                                    quantity=quantity,
                                    product_size=size,
                                )
                        order_line_item.save()  # Save each line item
                        logger.info(
                            f"Order line item saved for product"
                            f" {product.name}")
                    except Microcontroller.DoesNotExist:
                        messages.error(
                            request,
                            "One of the products in your bag wasn't found in"
                            " our database. Please call us for assistance.",
                        )
                        order.delete()
                        return redirect(reverse("view_bag"))

                # Save user info if 'save-info' was checked
                request.session["save_info"] = "save-info" in request.POST
                return redirect(reverse("checkout_success",
                                        args=[order.order_number])
                                )

            except Exception as e:
                logger.error(f"Error during checkout: {e}", exc_info=True)
                messages.error(
                    request, f"An error occurred during the checkout: {e}")
                if order.id:
                    order.delete()  # Roll back order if error occurs
                return redirect(reverse("view_bag"))

        else:
            messages.error(
                request,
                "There was an error with your form. Please double-check"
                " your information.",
            )

    else:
        bag = request.session.get("bag", {})
        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment.")
            return redirect(reverse("products"))

        current_bag = bag_contents(request)
        total = current_bag["grand_total"]
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            profile, created = UserProfile.objects.get_or_create(
                user=request.user)
            order_form = OrderForm(
                initial={
                    "full_name": profile.user.get_full_name(),
                    "email": profile.user.email,
                    "phone_number": profile.default_phone_number,
                    "country": profile.default_country,
                    "postcode": profile.default_postcode,
                    "town_or_city": profile.default_town_or_city,
                    "street_address1": profile.default_street_address1,
                    "street_address2": profile.default_street_address2,
                    "county": profile.default_county,
                }
            )
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(
            request,
            "Stripe public key is missing. Did you forget to set it"
            " in your environment?",
        )

    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """Handle successful checkouts."""
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile, created = UserProfile.objects.get_or_create(user=request.user)

        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                "default_phone_number": order.phone_number,
                "default_country": order.country,
                "default_postcode": order.postcode,
                "default_town_or_city": order.town_or_city,
                "default_street_address1": order.street_address1,
                "default_street_address2": order.street_address2,
                "default_county": order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(
        request,
        f"Order successfully processed! Your order number is {order_number}."
        f" A confirmation email will be sent to {order.email}.",
    )

    if "bag" in request.session:
        del request.session["bag"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
