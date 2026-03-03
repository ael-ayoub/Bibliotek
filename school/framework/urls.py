from django.urls import path

from . import views

urlpatterns = [
    path('cart/', views.getCart, name='get_cart'),
    path('cart-items/', views.getCartItems, name='get_cart_items'),
    path('cart-items/add/', views.addCartItem, name='add_cart_item'),
]