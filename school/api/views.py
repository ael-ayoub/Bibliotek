from django.shortcuts import render, get_object_or_404
from .models import posts
from django.http import JsonResponse
# Create your views here.
# def list_post(request):
def posts_view(request):
    if request.method == 'GET':
        Posts = posts.objects.all()
        return JsonResponse({"result": list(Posts.values("name", 'lastname', 'age'))})
    

def posts_viewPk(request, pk):
    data = get_object_or_404(posts, pk)

    result = {
        "name":data.name,
        "lastname":data.lastname,
        "age":data.age,
    }
    return JsonResponse(result);