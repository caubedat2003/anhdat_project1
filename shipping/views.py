from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Shipping
from .serializers import ShippingSerializer

class SelectShippingView(APIView):
    def post(self, request):
        customer_id = request.data.get("customer_id")
        order_id = request.data.get("order_id")
        address_id = request.data.get("address_id")
        method = request.data.get("method")

        if not all([customer_id, order_id, address_id, method]):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        shipping = Shipping.objects.create(
            customer_id=customer_id,
            order_id=order_id,
            address_id=address_id,
            method=method
        )

        return Response(ShippingSerializer(shipping).data, status=status.HTTP_201_CREATED)

class GetShippingView(APIView):
    def get(self, request, order_id):
        try:
            shipping = Shipping.objects.get(order_id=order_id)
            return Response(ShippingSerializer(shipping).data, status=status.HTTP_200_OK)
        except Shipping.DoesNotExist:
            return Response({"error": "Shipping not found"}, status=status.HTTP_404_NOT_FOUND)