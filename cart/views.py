from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_cart(request):
    """A view tat renders the shopping cart contents page"""
    return render(request, 'shoppingcart.html')


def add_to_cart(request, id):
    """Add a quantity of the specified item to te cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request):
    """Adjust the quantity of the specified item to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
    
