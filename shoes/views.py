from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Shoes
from .serializers import ShoesSerializer
from django.shortcuts import render

class ShoesListCreateAPIView(APIView):
    """ GET: List all shoes, POST: Create new shoes """
    def get(self, request):
        shoes = Shoes.objects.all()
        serializer = ShoesSerializer(shoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShoesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShoesDetailAPIView(APIView):
    """ GET: Retrieve shoes, PUT: Update shoes, DELETE: Delete shoes """
    def get_object(self, shoes_id):
        try:
            return Shoes.objects.get(id=shoes_id)
        except Shoes.DoesNotExist:
            return None

    def get(self, request, shoes_id):
        shoes = self.get_object(shoes_id)
        if not shoes:
            return Response({"error": "Shoes not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShoesSerializer(shoes)
        return Response(serializer.data)

    def put(self, request, shoes_id):
        shoes = self.get_object(shoes_id)
        if not shoes:
            return Response({"error": "Shoes not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShoesSerializer(shoes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, shoes_id):
        shoes = self.get_object(shoes_id)
        if not shoes:
            return Response({"error": "Shoes not found"}, status=status.HTTP_404_NOT_FOUND)
        shoes.delete()
        return Response({"message": "Shoes deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ShoesSearchAPIView(APIView):
    """ GET: Search for shoes by size, color, or brand """
    def get(self, request):
        query = request.query_params.get('title', None)
        if query:
            shoes = Shoes.objects.filter(title__icontains=query)
            serializer = ShoesSerializer(shoes, many=True)
            return Response(serializer.data)
        return Response({"error": "No search query provided"}, status=status.HTTP_400_BAD_REQUEST)
    
def shoes_detail_view(request):
    return render(request, 'shoes_detail.html')