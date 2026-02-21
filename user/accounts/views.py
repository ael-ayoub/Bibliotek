from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import login_info
from django.contrib.auth.models import User
# from django.forms.models import UserCreationForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get('password')

        # user = authenticate(email, password)
        user = authenticate(request, username = username, email=email,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else :
            return redirect("register")
    return render(request, "login.html",{'form': login_info})

def register_view(request):
    if request.user.is_authenticated:
        return redirect ('home')
    if request.method == 'POST':
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get('password')
        # should check bfore add:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        return redirect("home")
    return render(request, "register.html", {'form':login_info})

def home(request):
    if request.user.is_authenticated:
        return render (request, "home.html")
    return redirect ('login')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home")

def create_user(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        data = UserCreationForm(request.POST)
        # username = data.cleaned_data.get("username")
        print("im here")
        if data.is_valid():
            data.save()
            return redirect("login")
        # print (username)
        # if data.is_valid():
    else:

        print ("hello how are u ")
            # print(data)
        data = UserCreationForm()
    return render(request, "create_user.html", {"create_user_form":data})