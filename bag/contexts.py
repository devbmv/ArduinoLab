from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Microcontroller
from store_settings.models import ShippingSettings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    # Iterăm prin fiecare item din bag
    for item_id, item_data in bag.items():
        product = get_object_or_404(Microcontroller, pk=item_id)
        
        if isinstance(item_data, int):
            total += item_data * product.price  # Accesăm product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else: 
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price  # Accesăm product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    # Obținem setările de expediere din baza de date
    shipping_settings = ShippingSettings.objects.first()  # Ajustează pentru a selecta magazinul potrivit dacă ai mai multe
    
    # Verificăm dacă există shipping_settings, dacă nu, folosim valori implicite
    if shipping_settings is None:
        standard_shipping_cost = Decimal('5.00')  # Valoare implicită
        free_shipping_threshold = Decimal('50.00')  # Valoare implicită
    else:
        standard_shipping_cost = shipping_settings.standard_shipping_cost
        free_shipping_threshold = shipping_settings.free_shipping_threshold

    # Calculăm livrarea și pragul pentru livrare gratuită
    if total < free_shipping_threshold:
        delivery = standard_shipping_cost  # Livrare fixă, fără procent
        free_delivery_delta = free_shipping_threshold - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total if total>0 else 0

    # Contextul care va fi returnat
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_shipping_threshold': free_shipping_threshold,
        'grand_total': grand_total,
    }

    return context
