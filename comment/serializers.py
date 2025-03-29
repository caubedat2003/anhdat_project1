from rest_framework import serializers
from .models import Comment
from datetime import datetime

class CommentSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    product = serializers.CharField()
    customer_id = serializers.CharField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = datetime.utcnow()
        return Comment.objects.create(**validated_data)
