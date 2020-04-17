from django.shortcuts import render
from items.models import Item

# Create your views here.


def do_search(request):
    #Search function in the Navigation Bar
    items = Item.objects.filter(name__icontains=request.GET['q'])
    return render(request, "items.html", {"items": items})
    
