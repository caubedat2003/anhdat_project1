from django.urls import path
from .views import SelectShippingView
from django.shortcuts import render

urlpatterns = [
    path('shipping/', lambda request: render(request, 'shipping.html'), name='shipping_page'),
    path('api/shipping/select/', SelectShippingView.as_view(), name='select_shipping'),
]
