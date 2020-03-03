from django.shortcuts import get_object_or_404
from items.models import Item


def cart_contents(request):
    """Ensure that the shopping cart contents are available when rendering every page"""
    cart = request.session.get('cart', {})

    