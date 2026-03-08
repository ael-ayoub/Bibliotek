from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Author, Book, Student, Course
from .models import Author, Book, Student, Course, Category, Cotegories, Products
from .models import Post, Comment, Category, Tag, PostTag


def insert_students(request):
    Student.objects.create(name="ayoub")
    Student.objects.create(name="jamal")
    Student.objects.create(name="hamza")
    Student.objects.create(name="naima")
    Student.objects.create(name="lwalid")

    return JsonResponse({"success":"the studesnt insered successfully"})


def insert_courses(request):
    Course.objects.create(title="math")
    Course.objects.create(title="jo3rafia")
    Course.objects.create(title="tarbia 3la mowatana")
    Course.objects.create(title="arabic language")
    Course.objects.create(title="kofar language")

    return JsonResponse({"success":"Course successfully  insered!"})


def students(request):
    students = Student.objects.all()

    data = []
    for student in students:
        data.append({"name":student.name})
    test = Student.objects.get(id=2)
    print (test.courses.all())
    return JsonResponse({"studens":data})


def courses(request):
    courses = Course.objects.all()

    data = []
    for course in courses:
        data.append({"name":course.title})

    return JsonResponse({"courses":data})

def insert_course_to_student(request):
    student = Student.objects.get(id=2)
    student.courses.add(Course.objects.get(id=3))
    return redirect  (students)



def create_category(request):
    # Category.Ob cteate category with title and description
    Category.objects.create(title="technology", description="all about technology")
    return JsonResponse({"success":"category created successfully"})

# def create_product(request):
def create_post(request):
    post = Post(title="first post", content="this is the content of the first post", author=Author.objects.first(), category=Category.objects.first())
    if post.full_clean():   
        post.save()
    return JsonResponse({"success":"post created successfully"})


def create_comment(request):
    # create there comment 
    Comment.objects.create(content="this is a comment", post=Post.objects.first(), author=Author.objects.first())
    Comment.objects.create(content="this is a comment", post=Post.objects.first(), author=Author.objects.first())

    Comment.objects.create(content="this is a comment", post=Post.objects.first(), author=Author.objects.first())
    
    
    return JsonResponse({"success":"comment created successfully"})

def update_post(request):
    # post = Post.objects.first()
    # try to update all post draft with bulk
    Post.objects.filter(status="draft").update(status="published")
    return JsonResponse({"success":"post updated successfully"})

def increment_views(request):
    # post = Post.objects.first()
    # post.views_count += 1
    # post.save()
    # increment views count with bulk
    Post.objects.filter(id=1).update(views_count=F("views_count")+1)
    return JsonResponse({"success":"views count incremented successfully"})