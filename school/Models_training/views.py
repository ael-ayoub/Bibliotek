from django.shortcuts import render
# from dja/
from .models import user, Product
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from .models import ayoub

# return user as json
def model_view(request):
    users = user.objects.all()
    data = []
    for u in users:
        data.append({
            'name': u.name,
            'age': u.age
        })
    return JsonResponse(data, safe=False)

# in this view i will generate 1000 users with random names and ages and save them to the database
import random
import string
def model_view2(request):
    for i in range(1000):
        name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        age = random.randint(1, 100)
        user.objects.create(name=name, age=age)
    return JsonResponse({'message': '1000 users created'})



# set 20 product with real name in the databse 

def model_view3(request):
    products = [
        {'name': 'iPhone 12', 'price': 999, 'quantity': 10, 'slug': 'iphone-12'},
        {'name': 'Samsung Galaxy S21', 'price': 799, 'quantity': 20, 'slug': 'samsung-galaxy-s21'},
        {'name': 'Google Pixel 5', 'price': 699, 'quantity': 15, 'slug': 'google-pixel-5'},
        {'name': 'OnePlus 9', 'price': 729, 'quantity': 25, 'slug': 'oneplus-9'},
        {'name': 'Sony Xperia 1 II', 'price': 1199, 'quantity': 5, 'slug': 'sony-xperia-1-ii'},
        {'name': 'LG Velvet', 'price': 599, 'quantity': 30, 'slug': 'lg-velvet'},
        {'name': 'Motorola Edge Plus', 'price': 999, 'quantity': 10, 'slug': 'motorola-edge-plus'},
        {'name': 'Nokia 8.3', 'price': 699, 'quantity': 20, 'slug': 'nokia-8-3'},
        {'name': 'Asus ROG Phone 5', 'price': 999, 'quantity': 15, 'slug': 'asus-rog-phone-5'},
        {'name': 'Xiaomi Mi 11', 'price': 749, 'quantity': 25, 'slug': 'xiaomi-mi-11'},
    ]
    for p in products:
        Product.objects.create(name=p['name'], price=p['price'], quantity=p['quantity'], slug=p['slug'])
    return JsonResponse({'message': f'{len(products)} products created'})

def model_view4(request):
    products = Product.objects.all()
    data = []
    for p in products:
        data.append({
            'name': p.name,
            'price': p.price,
            'quantity': p.quantity,
            'slug': p.slug
        })
    return JsonResponse(data, safe=False)

# here i will test slug field by getting product by slug and return it as json

def model_view5(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        data = {
            'name': product.name,
            'price': product.price,
            'quantity': product.quantity,
            'slug': product.slug
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'Product not found'}, status=404)


def insert_data(request):
    try:
        phone1  = Product(name='iPhone 13', price=999, quantity=10, slug='iphone-133')
        phone2 = Product(name='iPhone 143', price=1099, quantity=5, slug='iphone-12')
        # print(phone1)
        # phone1.full_clean()  # This will run the model's validation, including unique constraints
        # phone2.full_clean()  # This will run the model's validation, including unique constraints
        # phone1.save()
        phone2.save()
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse({'message': 'Data inserted'}, status=201)
    # user.objects.create(name='John Doe', age=30)
    # return JsonResponse({'message': 'Data inserted'})



def insert_ayoubat(request):
    ayoubat={
        "ayoub", "maaee", "jamal", "achraf"
    }
    for a in ayoubat:
        ayoub.objects.create(name=a)

    return JsonResponse({"seccuss": "data added successfully"})


def get_ayoubat(request):
    ayoubat = ayoub.objects.all()
    for a in ayoubat:
        print (a.name)

    return JsonResponse({})