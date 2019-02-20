from django.urls import include, path
from .views import (
    dynamic_lookup_view, 
    product_create_view, 
    product_delete_view, 
    product_list_view
)

urlpatterns = [
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('create/', product_create_view),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('', product_list_view, name='product-list')
    ]
