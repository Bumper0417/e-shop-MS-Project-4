from django.shortcuts import render
from items.models import Item

# Create your views here.


def index(request):
    """A view displays the index page"""

    # To find the first three ordered by the lowest price: 
    items = Item.objects.all().order_by('price')[:3]

    return render(request, "index.html", {"items": items})
    