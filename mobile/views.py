from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Mobile
from .serializers import MobileSerializer

class MobileListCreateAPIView(APIView):
    """ GET: List all mobiles, POST: Create a new mobile """
    def get(self, request):
        mobiles = Mobile.objects.all()
        serializer = MobileSerializer(mobiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MobileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MobileDetailAPIView(APIView):
    """ GET: Retrieve a mobile, PUT: Update a mobile, DELETE: Delete a mobile """
    def get_object(self, mobile_id):
        try:
            return Mobile.objects.get(id=mobile_id)
        except Mobile.DoesNotExist:
            return None

    def get(self, request, mobile_id):
        mobile = self.get_object(mobile_id)
        if not mobile:
            return Response({"error": "Mobile not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MobileSerializer(mobile)
        return Response(serializer.data)

    def put(self, request, mobile_id):
        mobile = self.get_object(mobile_id)
        if not mobile:
            return Response({"error": "Mobile not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MobileSerializer(mobile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, mobile_id):
        mobile = self.get_object(mobile_id)
        if not mobile:
            return Response({"error": "Mobile not found"}, status=status.HTTP_404_NOT_FOUND)
        mobile.delete()
        return Response({"message": "Mobile deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class MobileSearchAPIView(APIView):
    """ GET: Search for mobiles by brand or model """
    def get(self, request):
        query = request.query_params.get('title', None)
        if query:
            mobiles = Mobile.objects.filter(title__icontains=query)
            serializer = MobileSerializer(mobiles, many=True)
            return Response(serializer.data)
        return Response({"error": "No search query provided"}, status=status.HTTP_400_BAD_REQUEST)