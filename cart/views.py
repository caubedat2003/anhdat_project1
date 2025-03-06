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

    def get(self, request, customer_id):
        """ Retrieve all cart items for a specific customer """
        cart_items = Cart.objects.filter(customer_id=str(customer_id))
        cart_data = []

        for item in cart_items:
            product = Product.objects(id=ObjectId(item.product_id)).first()
            if product:
                cart_data.append({
                    "id": str(item.id),
                    "product_id": item.product_id,
                    "title": product.title,
                    "price": float(product.price),
                    "quantity": item.quantity,
                    "total_price": float(item.total_price),
                    "image": product.image  # Assuming product has an image field
                })

        return Response(cart_data, status=status.HTTP_200_OK)
    
class UpdateCartView(APIView):
    def patch(self, request, cart_id):
        try:
            cart_item = Cart.objects.get(id=cart_id)
            change = int(request.data.get("change", 0))
            
            if change != 0:
                cart_item.quantity += change
                if cart_item.quantity < 1:
                    cart_item.delete()
                else:
                    cart_item.save()
            
            return Response({"message": "Quantity updated"}, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)
        
class DeleteCartView(APIView):
    def delete(self, request, cart_id):
        """ Remove an item from the cart """
        try:
            cart_item = Cart.objects.get(id=cart_id)
            cart_item.delete()
            return Response({"message": "Item removed successfully"}, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)
