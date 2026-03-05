from django.urls import path
from .views import create, update, delete , get_one , get_all, delete_all

# create path for each function in views.py

urlpatterns = [
    path ("create/", create),
    path ("update/<int:pk>/", update),
    path ("delete/<int:pk>/", delete),
    path ("get/<int:pk>/", get_one),
    path ("get_all/", get_all),
    path ("delete_all/", delete_all),
    # path ("delele_all", ),
]