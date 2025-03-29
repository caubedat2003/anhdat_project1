from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from bson import ObjectId
from .models import Comment
from .serializers import CommentSerializer

class CommentListAPIView(APIView):
    def get(self, request, product_id):
        try:
            comments = Comment.objects(product=ObjectId(product_id))  # Ensure proper ID filtering
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class AddCommentAPIView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.create(serializer.validated_data)
            return Response({"message": "Comment added successfully!", "comment": CommentSerializer(comment).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
