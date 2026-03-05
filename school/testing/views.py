from django.shortcuts import render
from django.http import JsonResponse
from .models import Users
# Create your views here.
def get_one(request, pk):
    try:
        user = Users.objects.get(id=pk)
        data = {u.id:{u.name,u.age} for u in user}
        return JsonResponse(data)
    except Exception as e:
        print (f"You have Error:  {str(e)}")
    return JsonResponse({"Error":"user do not exsit in database from get function!"})

def update(request, pk):
    try:
        user = Users.objects.get(id=pk)
    except Exception as e:
        error = f"the user of id \'{pk}\' do not exsit in database"
        print (error)
        return JsonResponse({"Error":error})
    JsonResponse({"success": "The user information Update successfully"})

def delete(request, pk):
    try:
        user = Users.objects.get(id=pk)
    except Exception as e:
        error = f"the user of id \'{pk}\' do not exsit in database"
        print (error)
        return JsonResponse({"Error":error})
    user.delete()
    JsonResponse({"success": "The user was deleted successfully"})

def delete_all(request):
    Users.objects.all().delete()
    return JsonResponse({"Success":"All the user are deleted successfully"})

def get_all(request):
    users = Users.objects.all()
    data = {u.id:{"name":u.name,"age":u.age} for u in users}
    # if type(data) is dict:
        # return JsonResponse({"Yes":f"data type is Dict {type(data)}"})
    return JsonResponse(data)

def create(request):
    users = [["ayoub", 33], ["achraf", 3], ["naima", 55], ["jamal", 44]]
    for user in users:
        Users.objects.create(name=user[0], age=user[1])
    return JsonResponse({"success": "Data submmited Successfully"})