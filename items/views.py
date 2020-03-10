from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.


def all_items(request):
    items = Item.objects.all()
    return render(request, "items.html", {"items": items})


def item_detail(request, pk):
    """Create a view that returns a single
    Item object based on the item ID (pk) and
    render it to the 'itemdetail.html' template.
    Or return a 404 error if the item is
    not found"""
    item = get_object_or_404(Item, pk=pk)
    # Pass an item from the view to the template `{"item": item}`
    return render(request, "itemdetail.html", {"item": item})


def category_choice(request, category_choice):
    """Create a view that returns Items from a specific Category based on the category ID (pk)
    and renders it to the "items.html" template"""
    category_choice = Item.objects.filter(categories=category_choice)
    return render(request, "items.html", {"items": category_choice})
