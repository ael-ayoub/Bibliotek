from django.urls import path
from . import views

urlpatterns = [
    path('insert_course/', views.insert_courses),
    path('insert_students/', views.insert_students),
    path('courses/', views.courses),
    path('students/', views.students),
    path('', views.insert_course_to_student)
]  