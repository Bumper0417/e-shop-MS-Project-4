from django.shortcuts import get_object_or_404
from items.models import Item


def cart_contents(request):
    """Ensure that the shopping cart contents are available when rendering every page"""
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    item_count = 0
    for id, quantity in cart.items():
        item = get_object_or_404(Item, pk=id)
        total += quantity * item.price
        item_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'item': item})
    return {'cart_items': cart_items, 'total': total, 'item_count': item_count}
    
