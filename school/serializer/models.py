from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=122)

class Product(models.Model):
    name = models.CharField(max_length=122)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null= True)