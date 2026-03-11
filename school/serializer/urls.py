from django.urls import path , include
from . import views


urlpatterns = [
    # path ('home/', views.home),
    path ('insert_cat/', views.insert_cat),
    path ('insert_pro/', views.insert_pro),
    path ('categories/', views.categories),
    path ('products/', views.products),
    # path ('home/', views.get_cat),
]