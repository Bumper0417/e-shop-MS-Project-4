from django.shortcuts import render, Http404
from items.models import Item

# Create your views here.


def do_search(request):
    
    items = Item.objects.filter(name__icontains=request.GET['q'])
    if 'q' in request.GET:
        return render(request, "items.html", {"items": items})
    elif 'q' == None:
        return Http404('Enterr your search criteria')
    else:
        return Http404('Item not found!')
    
