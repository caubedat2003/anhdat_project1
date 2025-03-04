from rest_framework import serializers
from .models import Shoes

class ShoesSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock = serializers.IntegerField()
    image = serializers.CharField(allow_blank=True)
    brand = serializers.CharField(max_length=255)
    size = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Shoes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
