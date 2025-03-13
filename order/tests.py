from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from cart.models import Cart
from product.models import Product
from bson import ObjectId
from .serializers import OrderSerializer

class CreateOrderView(APIView):
    def post(self, request):
        customer_id = str(request.data.get("customer_id"))

        # Get all cart items
        cart_items = Cart.objects.filter(customer_id=customer_id)
        if not cart_items.exists():
            return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        # Calculate total price
        total_price = sum(float(item.total_price) for item in cart_items)

        # Create an order
        order = Order.objects.create(customer_id=customer_id, total_price=total_price)

        # Move cart items to OrderItem
        order_items = []
        for item in cart_items:
            product = Product.objects(id=ObjectId(item.product_id)).first()
            if product:
                order_items.append(OrderItem(
                    order=order,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    total_price=item.total_price
                ))

        # Bulk insert OrderItem
        OrderItem.objects.bulk_create(order_items)

        # Clear cart
        cart_items.delete()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

class OrderDetailView(APIView):
    def get(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
            return Response(OrderSerializer(order).data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
