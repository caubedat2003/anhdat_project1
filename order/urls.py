from django.urls import path
from .views import CreateOrderView, OrderDetailView

urlpatterns = [
    path('api/order/create/', CreateOrderView.as_view(), name='create_order'),
    path('api/order/<str:order_id>/', OrderDetailView.as_view(), name='order_detail'),
]
