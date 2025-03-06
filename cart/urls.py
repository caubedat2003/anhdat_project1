from django.urls import path
from .views import CartView, UpdateCartView, DeleteCartView
from django.shortcuts import render

urlpatterns = [
    path('cart/', lambda request: render(request, 'cart.html'), name='cart_page'),
    path('api/cart/', CartView.as_view(), name='cart_api'),
    path('api/cart/<str:customer_id>/', CartView.as_view(), name='view_cart'),
    path('api/cart/update/<str:cart_id>/', UpdateCartView.as_view(), name='update_cart'),
    path('api/cart/delete/<str:cart_id>/', DeleteCartView.as_view(), name='delete_cart'),
]