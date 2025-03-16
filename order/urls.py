from django.urls import path
from django.shortcuts import render
from .views import CreateOrderView, OrderDetailView, OrderItemView

urlpatterns = [
    path('order/', lambda request: render(request, 'order.html'), name='order-page'),
    path('api/order/create/', CreateOrderView.as_view(), name='create_order'),
    path('api/order/<str:order_id>/', OrderDetailView.as_view(), name='order_detail'),
    path('api/order/items/<str:order_id>/', OrderItemView.as_view(), name='order_items'),
]
