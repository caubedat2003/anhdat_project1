from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from cart.models import Cart
from shipping.models import Shipping
from customer.models import Address , Customer
from paying.models import Paying
from product.models import Product
from bson import ObjectId
from django.db import transaction
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class CreateOrderView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        
        customer_id = request.data.get("customer_id")
        order_date = request.data.get("order_date")
        total_price = request.data.get("total_price")
        address_id = request.data.get("address_id")
        shipping_method = request.data.get("shipping_method")
        transaction_id = request.data.get("transaction_id")

        # Validate required data
        if not all([customer_id, total_price, address_id, shipping_method, transaction_id]):
            return Response({"error": "Missing required data"}, status=status.HTTP_400_BAD_REQUEST)

        # Get all cart items
        cart_items = Cart.objects.filter(customer_id=customer_id)
        if not cart_items.exists():
            return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():  # Ensures all operations succeed or rollback
                # Create Order
                order = Order.objects.create(
                    customer_id=customer_id,
                    total_price=total_price,
                    order_date=order_date,
                    status="delivering"
                )

                # Create Order Items
                order_items = []
                for item in cart_items:
                    product = Product.objects(id=ObjectId(item.product_id)).first()
                    if product:
                        order_items.append(OrderItem(
                            order=order,
                            product_id=item.product_id,
                            title=product.title,
                            price=item.total_price,
                            quantity=item.quantity,
                            total_price=item.total_price
                        ))

                OrderItem.objects.bulk_create(order_items)

                # Create Shipping
                shipping = Shipping.objects.create(
                    customer_id=customer_id,
                    address_id=address_id,
                    method=shipping_method,
                    order=order
                )

                # Create Paying
                paying = Paying.objects.create(
                    order=order,
                    payment_method="PayPal",
                    payment_status="Completed",
                    transaction_id=transaction_id,
                    payment_date=order_date
                )

                # Clear Cart
                cart_items.delete()

                return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class OrderDetailView(APIView):
    def get(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
            return Response(OrderSerializer(order).data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        
class OrderItemView(APIView):
    def get(self, request, order_id):
        try:
            order_items = OrderItem.objects.filter(order_id=order_id)
            return Response(OrderItemSerializer(order_items, many=True).data, status=status.HTTP_200_OK)
        except OrderItem.DoesNotExist:
            return Response({"error": "Order items not found"}, status=status.HTTP_404_NOT_FOUND)
