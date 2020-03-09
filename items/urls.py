from django.conf.urls import url, include
from .views import all_items, item_detail

urlpatterns = [
    url(r'^$', all_items, name='items'),
    # Pass a value from the template into the view
    url(r'^(?P<pk>\d+)', item_detail, name='item_detail'),
]
