from django.conf.urls import url

from .views import (
        cart_home, 
        cart_update, 
        checkout_home,
        checkout_done_view,
        cart_update_seller,
        quantity_add,
        quantity_subtract
        )

urlpatterns = [
    url(r'^$', cart_home, name='home'),
    url(r'^add/', quantity_add, name='add'),
    url(r'^subtract/', quantity_subtract, name='subtract'),
    url(r'^checkout/success/$', checkout_done_view, name='success'),
    url(r'^checkout/$', checkout_home, name='checkout'),
    url(r'^update/$', cart_update, name='update'),
    url(r'^update-seller/$', cart_update_seller, name='update-seller'),
]