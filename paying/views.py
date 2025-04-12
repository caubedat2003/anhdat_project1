from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Paying
from .serializers import PayingSerializer
from django.shortcuts import render

class PayingListCreateAPIView(APIView):
    """ GET: List all books, POST: Create a new book """
    def get(self, request):
        payings = Paying.objects.all()
        serializer = Paying(payings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PayingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)