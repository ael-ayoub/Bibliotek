from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .serializer import products_serializer, categories_serializer
from .models import Product, Category

def insert_cat(re):
    Category.objects.create(title="iphones")
    Category.objects.create(title="samsung")
    Category.objects.create(title="xiaomi")


def insert_pro(re):
    Product.objects.create(name="iphone-12", price=444, Category=1)
    Product.objects.create(name="samsung s-22 ultra", price=555, Category=2)
    Product.objects.create(name="samsung A-12 core", price= 300, Category=2)
    Product.objects.create(name= "readme note 14 pro", price=2000, Category=3)
    Product.objects.create(name = "iphone 12", price =400, Category=1)

def products(request):
    ps = Product.objects.all()

    response = products_serializer(ps, many= True)
    
    return Response(response.data)

def categories(request):
    cs = Category.objects.all()
    response = categories_serializer(cs, many=True)

    return Response(response.data)