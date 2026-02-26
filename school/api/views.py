from django.shortcuts import render,redirect
from .forms import PostForm, ComentForm
from .models import Post, Comments
from django.conf.urls import handler400


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