from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product
def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })
    shipping_settings = getattr(request, 'shipping_settings', None)

    if shipping_settings:
        free_shipping_threshold = shipping_settings.free_shipping_threshold
        standard_shipping_cost = shipping_settings.standard_shipping_cost
    else:
        # Fallback pentru transport în cazul în care shipping_settings este None
        free_shipping_threshold = Decimal('50.00')  # Valoare implicită
        standard_shipping_cost = Decimal('5.00')  # Valoare implicită

    if total < free_shipping_threshold :
        delivery = standard_shipping_cost
        free_delivery_delta = free_shipping_threshold - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': free_shipping_threshold,
        'grand_total': grand_total,
    }

    return context