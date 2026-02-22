from django.shortcuts import render
# from rest_framework import generics
# from .models import BlogPost
# from .serializers import BlogPostSerializer

# class BlogPostListCreate(generics.ListCreateAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer
# # Create your views here.

from rest_framework.decorators import api_view
from rest_framework import status
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.response import Response

# what im doing here ??
# i want to create reast api ?? 
# what i need ??




@api_view(['GET','POST'])
def blogs(request):
    if request.method == 'GET':
        blogs = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogs, many=True)
        return Response(serializer.data) 
    if request.method == "POST":
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

