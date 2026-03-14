from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def test_view(request):
    data_test = {
        "name": "John Doe",
        "age": 30,
    }
    return Response(data_test)


@api_view(['GET'])
def test_view(request):
    data_test = [
        {"name": "John Doe", "age": 30},
        {"name": "Sara", "age": 25},
    ]
    return Response(data_test)