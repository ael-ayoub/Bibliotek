from django.db import models

# Create your models here.

class Cart(models.Model):
    user = models.CharField(max_length=100)
    def __self__(self):
        return self.name
    
class CartItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    def __self__(self):
        return self.name
    
    