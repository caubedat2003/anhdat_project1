from django.urls import path
from django.shortcuts import render
from .views import PayingListCreateAPIView

urlpatterns = [
    path('payment/', lambda request: render(request, 'payment.html'), name='payment_page'),
    path('api/payments/', PayingListCreateAPIView.as_view(), name='payment_api'),
]
