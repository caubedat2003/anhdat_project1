from django.urls import path
from .views import cart_list_page, get_cart_items

urlpatterns = [
    path('cart/', cart_list_page, name='cart_list_page'),  
    path('api/cart/', get_cart_items, name='get_cart_items'),  
]