from django.urls import path, include
from .views import login_view, register_view, home, logout_view , create_user

urlpatterns = [
    path("", home, name="home"),
    path ("login/", login_view, name="login"),
    path ("register/", register_view, name="register"),
    path ("home/", home, name="home"),
    path("logout/", logout_view, name="logout"),
    path ("create/", create_user, name="create_user")
]