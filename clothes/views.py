from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Clothes
from .serializers import ClothesSerializer
from django.shortcuts import render

class ClothesListCreateAPIView(APIView):
    """ GET: List all clothes, POST: Create new clothes """
    def get(self, request):
        clothes = Clothes.objects.all()
        serializer = ClothesSerializer(clothes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClothesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClothesDetailAPIView(APIView):
    """ GET: Retrieve clothes, PUT: Update clothes, DELETE: Delete clothes """
    def get_object(self, clothes_id):
        try:
            return Clothes.objects.get(id=clothes_id)
        except Clothes.DoesNotExist:
            return None

    def get(self, request, clothes_id):
        clothes = self.get_object(clothes_id)
        if not clothes:
            return Response({"error": "Clothes not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClothesSerializer(clothes)
        return Response(serializer.data)

    def put(self, request, clothes_id):
        clothes = self.get_object(clothes_id)
        if not clothes:
            return Response({"error": "Clothes not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClothesSerializer(clothes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, clothes_id):
        clothes = self.get_object(clothes_id)
        if not clothes:
            return Response({"error": "Clothes not found"}, status=status.HTTP_404_NOT_FOUND)
        clothes.delete()
        return Response({"message": "Clothes deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ClothesSearchAPIView(APIView):
    """ GET: Search for clothes by size or color """
    def get(self, request):
        query = request.query_params.get('title', None)
        if query:
            clothes = Clothes.objects.filter(title__icontains=query)
            serializer = ClothesSerializer(clothes, many=True)
            return Response(serializer.data)
        return Response({"error": "No search query provided"}, status=status.HTTP_400_BAD_REQUEST)

def clothes_detail_view(request):
    return render(request, 'clothes_detail.html')