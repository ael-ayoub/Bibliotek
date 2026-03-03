from django.shortcuts import render
# from rest_framework.views import api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart, CartItems
from .serializers import CartSerializer, CartItemSerializer
# from rest_framework import get
from django.shortcuts import get_object_or_404
# Create your views here.


# create two models cart and cart items: each one with fields and with relations between them -> cart has many cartIteems
@api_view(['GET'])
def getCart(request):
    # cart = Cart.objects.first()
    try:
        cart = Cart.objects.get(id=1)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=404)
    cart_items = CartItems.objects.filter(cart=cart)
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCartItems(request):
    cart_items = CartItems.objects.all()
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addCartItem(request):
    # cart = get_object_or_404(id = 1)
    # cart = get_object_or_create
    cart = Cart.objects.get_or_create(user = "ahmed")
    # cart = Cart.objects.first()  # Assuming you want to add items to the first cart
    # if not cart:
    #     return Response({"error": "Cart not found"}, status=404)
    serializer = CartItemSerializer(data=request.data)
    # serializer = CartItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

