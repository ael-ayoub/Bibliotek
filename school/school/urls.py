"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from Models_training.views import model_view as users
from Models_training.views import model_view2 as generate_users
from Models_training.views import model_view3 as generate_products
from Models_training.views import model_view4 as get_products
# from Models_training import views.
# include slug
from Models_training.views import model_view5 as get_product_by_slug
from Models_training.views import insert_data, insert_ayoubat,get_ayoubat

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include ('api.urls')),
    path('framework/', include('framework.urls')),
    path('users/', users),
    path('generate-users/', generate_users),
    path('generate-products/', generate_products),
    path('products/', get_products),
    path('products/<slug:slug>/', get_product_by_slug),
    path('insert-data/', insert_data),
    path('insert', insert_ayoubat),
    path('getdata/', get_ayoubat),
]
