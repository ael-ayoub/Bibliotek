from rest_framework import serializers
from .models import Product, Category

class categories_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class products_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"