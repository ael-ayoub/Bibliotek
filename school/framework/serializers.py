from .models import Cart, CartItems
from rest_framework import serializers

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    # items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'