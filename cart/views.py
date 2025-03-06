from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart
from product.models import Product  # Import MongoDB model
from bson import ObjectId

class CartView(APIView):
    
    def post(self, request):
        try:
            customer_id = str(request.data.get("customer_id"))  # Convert to string
            product_id = request.data.get("product_id")  # Expect MongoDB ObjectID
            quantity = int(request.data.get("quantity", 1))

            # Validate Product from MongoDB
            product = Product.objects(id=ObjectId(product_id)).first()
            if not product:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

            # Ensure customer_id is stored as string
            cart_item, created = Cart.objects.get_or_create(
                customer_id=str(customer_id),  # Ensure string format
                product_id=str(product_id)
            )
            if not created:
                cart_item.quantity += quantity
            cart_item.save()

            return Response({"message": "Added to cart"}, status=status.HTTP_201_CREATED)

        except ValueError:
            return Response({"error": "Invalid data format"}, status=status.HTTP_400_BAD_REQUEST)
