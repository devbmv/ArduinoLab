from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Microcontroller
from store_settings.models import ShippingSettings


def bag_contents(request):
    """
    This function calculates the contents of a shopping bag, including the
      total cost, 
    product count, delivery cost, and grand total. It also determines the
      remaining amount 
    needed for free shipping.

    Parameters:
    request (HttpRequest): The request object containing the session data.

    Returns:
    dict: A dictionary containing the following keys:
        - bag_items: A list of dictionaries, each representing an item in 
        the bag.
        - total: The total cost of all items in the bag.
        - product_count: The total number of products in the bag.
        - delivery: The cost of delivery.
        - free_delivery_delta: The remaining amount needed for free shipping.
        - free_shipping_threshold: The threshold amount for free shipping.
        - grand_total: The total cost including delivery.
    """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get("bag", {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Microcontroller, pk=item_id)

        if isinstance(item_data, int):
            total += item_data * product.price
            product_count += item_data
            bag_items.append(
                {
                    "item_id": item_id,
                    "quantity": item_data,
                    "product": product,
                }
            )
        else:
            for size, quantity in item_data["items_by_size"].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append(
                    {
                        "item_id": item_id,
                        "quantity": quantity,
                        "product": product,
                        "size": size,
                    }
                )

    shipping_settings = ShippingSettings.objects.first()

    if shipping_settings is None:
        standard_shipping_cost = Decimal("5.00")
        free_shipping_threshold = Decimal("50.00")
    else:
        standard_shipping_cost = shipping_settings.standard_shipping_cost
        free_shipping_threshold = shipping_settings.free_shipping_threshold

    if total < free_shipping_threshold:
        delivery = standard_shipping_cost
        free_delivery_delta = free_shipping_threshold - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total if total > 0 else 0

    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_shipping_threshold": free_shipping_threshold,
        "grand_total": grand_total,
    }

    return context
def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get("bag", {})


    for item_id, item_data in bag.items():
        product = get_object_or_404(Microcontroller, pk=item_id)

        if isinstance(item_data, int):
            total += item_data * product.price  
            product_count += item_data
            bag_items.append(
                {
                    "item_id": item_id,
                    "quantity": item_data,
                    "product": product,
                }
            )
        else:
            for size, quantity in item_data["items_by_size"].items():
                total += quantity * product.price  
                product_count += quantity
                bag_items.append(
                    {
                        "item_id": item_id,
                        "quantity": quantity,
                        "product": product,
                        "size": size,
                    }
                )

    shipping_settings = (
        ShippingSettings.objects.first()
    )  

    if shipping_settings is None:
        standard_shipping_cost = Decimal("5.00") 
        free_shipping_threshold = Decimal("50.00") 
    else:
        standard_shipping_cost = shipping_settings.standard_shipping_cost
        free_shipping_threshold = shipping_settings.free_shipping_threshold

    if total < free_shipping_threshold:
        delivery = standard_shipping_cost 
        free_delivery_delta = free_shipping_threshold - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total if total > 0 else 0

    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_shipping_threshold": free_shipping_threshold,
        "grand_total": grand_total,
    }

    return context
