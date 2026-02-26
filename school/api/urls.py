from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('form/', views.form, name="form"),
    path('create/', views.create_post_view, name="create"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('comment/', views.create_comment, name="create_comment")
]
