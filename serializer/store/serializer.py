from rest_framework import serializers
from .models import Product, Category

class products_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class categories_serializer(serializers.ModelSerializer):
    # test = serializers.CharField()
    products = products_serializer(many =True)
    class Meta:
        model = Category
        fields = "__all__"


class products_serializer(serializers.ModelSerializer):
    category = categories_serializer()
    class Meta:
        model = Product
        fields = "__all__"