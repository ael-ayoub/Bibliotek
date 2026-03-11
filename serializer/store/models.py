from django.db import models

# Create your models here.

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=122, unique=True)

class Product(models.Model):
    name = models.CharField(max_length=122, unique=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null= True, related_name="products")