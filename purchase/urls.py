from django.urls import path
from .views import add_to_shopping_cart,remove_from_shopping_cart,shopping_cart,confirm_order


#http://localhost:8000/purchase/
urlpatterns = [
    path('add_to_shopping_cart/', add_to_shopping_cart, name='add_to_shopping_cart'),
    path('remove_from_shopping_cart/', remove_from_shopping_cart, name='remove_from_shopping_cart'),
    path('shopping_cart/', shopping_cart, name='shopping_cart'),
    path('confirm_order/', confirm_order, name='confirm_order'),
    
]