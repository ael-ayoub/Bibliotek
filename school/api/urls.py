from django.urls import path
from .views import posts_view, posts_viewPk
urlpatterns = [
    path("posts/", posts_view, name="posts_view"),
    path("posts/<int,pk>", posts_viewPk, name="posts_view"),
]
