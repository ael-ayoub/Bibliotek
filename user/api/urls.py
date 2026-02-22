from django.urls import path , include
from views import blogs


urlpatterns = [
    path ("blogs", blogs, name = "blogs" )
]