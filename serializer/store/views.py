from django.shortcuts import render
from rest_framework.decorators import api_view, APIView
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .serializer import products_serializer, categories_serializer
from .models import Product, Category

@api_view(['GET'])
def insert_cat(re):
    try:

        Category.objects.create(title="iphones")
        Category.objects.create(title="samsung")
        Category.objects.create(title="xiaomi")
    except Exception as e:
        return HttpResponse("categories already exist")
    return HttpResponse("categories was created successfully")


@api_view(['GET'])
def insert_pro(re):
    try:
        Product.objects.create(name="iphone-12", price=444, category = Category.objects.get(id=1))
        Product.objects.create(name="samsung s-22 ultra", price=555, category = Category.objects.get(id=2))
        Product.objects.create(name="samsung A-12 core", price= 300, category = Category.objects.get(id=2))
        Product.objects.create(name= "readme note 14 pro", price=2000, category = Category.objects.get(id=3))
        Product.objects.create(name = "iphone 18", price =400, category = Category.objects.get(id=1))
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse("Products was create successfully")

@api_view(['GET'])
def products(request):
    ps = Product.objects.all()

    response = products_serializer(ps, many= True)
    
    return Response(response.data)

@api_view(['GET'])
def categories(request):
    cs = Category.objects.all()
    response = categories_serializer(cs, many=True)
    print ("*"*120)
    print (response.data[0]["id"])
    print ("*"*120)
    return Response(response.data)


class Test_view(APIView):
    def Get(self, request):
        return Response({"hello":"it is from allah hamdollah"})
    
    def delete(self, request):
        return Response({"messge:":"this from delete method"})