from django.shortcuts import render
from items.models import Item

# Create your views here.


def do_search(request):
    items = Item.objects.filter(name__icontains=request.GET['q'])
    return render(request, "items.html", {"items": items})
