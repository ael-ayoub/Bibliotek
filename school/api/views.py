from django.shortcuts import render,redirect
from .forms import PostForm, ComentForm
from .models import Post, Comments
from django.conf.urls import handler400
from django.http import JsonResponse
# from rest_framework import api
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from .serializer import post_as_json


def home(request):
    return render (request, "home.html")


def form(request):
    if request.method == "GET":
        posts = Post.objects.all()
        comments = Comments.objects.all()
    
    context = {
        "posts":posts,
        "comments":comments
    }
    return render(request, "forms.html", context)

def create_post_view(request):
    success = False
    if request.method == "POST":
        post = PostForm(request.POST)
        if post.is_valid():
            post.save()
            success = True

    post = PostForm()
    contex = {
        "success": success,
        "form":post,
    }
    return render (request, "create_post.html", contex)


def delete(request, pk):
    post_del = Post.objects.filter(id=pk)
    if post_del is not None:
        post_del.delete()
    return redirect('form')

def create_comment(request):
    success = False
    if request.method == 'POST':
        comment = ComentForm(request.POST)
        if comment.is_valid():
            comment.save()
            success = True
    comments = ComentForm()
    context = {
        "success":success,
        "form":comments,
    }
    return render(request, "create_comment.html", context)

# @post
@api_view(['GET'])
def json_view(request):
    posts = Post.objects.all()
    posts_serializer = post_as_json(posts, many=True)
    return Response(posts_serializer.data)