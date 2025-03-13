from rest_framework import serializers
from .models import Order, OrderItem
from cart.models import Cart
from product.models import Product
from bson import ObjectId

class OrderItemSerializer(serializers.ModelSerializer):
    product_details = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'product_id', 'quantity', 'total_price', 'product_details']

    def get_product_details(self, obj):
        product = Product.objects(id=ObjectId(obj.product_id)).first()
        if product:
            return {
                "title": product.title,
                "price": float(product.price),
                "image": product.image
            }
        return None

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer_id', 'order_date', 'total_price', 'status', 'order_items']
