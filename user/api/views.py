from django.shortcuts import render
# from rest_framework import generics
# from .models import BlogPost
# from .serializers import BlogPostSerializer

# class BlogPostListCreate(generics.ListCreateAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer
# # Create your views here.

from rest_framework.decorators import api_view
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.response import Response

# what im doing here ??
# i want to create reast api ?? 
# what i need ??




@api_view(['GET'])
def blogs(request):
    blogs = BlogPost.objects.all()
    serializer = BlogPostSerializer(blogs, many=True)
    return Response(serializer.data) 