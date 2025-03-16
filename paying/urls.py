from django.urls import path
from django.shortcuts import render

urlpatterns = [
    path('payment/', lambda request: render(request, 'payment.html'), name='payment_page'),
]
