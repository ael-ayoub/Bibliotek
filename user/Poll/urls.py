from django.urls import path
from .views import poll_view, poll_create


urlpatterns = [
    path ('create/', poll_create, name="poll_create"),
    path ('view/', poll_view, name ="poll_view"),
]
