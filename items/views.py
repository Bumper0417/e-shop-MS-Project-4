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
