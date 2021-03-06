from django.shortcuts import render, redirect, reverse
from items.models import Item

# Create your views here.


def view_cart(request):
    """A view tat renders the shopping cart contents page"""

    items = Item.objects.all().order_by('-price')[:3]
    return render(request, 'cart.html', {"items": items})


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('items'))
    

def adjust_cart(request, id):
    """Adjust the quantity of the specified item to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    