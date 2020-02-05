from django.conf.urls import url

from .views import (
        ProductListView, 
        ProductDetailSlugView, 
        ProductDownloadView,
        product_detail_view,
        product_add,
        product_add_existing,
        product_list_view,
        )

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    #url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/$', product_detail_view, name='detail'),
    url(r'^(?P<slug>[\w-]+)/(?P<pk>\d+)/$', ProductDownloadView.as_view(), name='download'),
    url(r'^add/', product_add, name='product_add'),
    url(r'^add_existing/', product_add_existing, name='product_add_existing'),
]

