from django.db import models
from django.db.models import Model, CharField, IntegerField, SlugField
# Create your models here.
class user(Model):
    name = CharField(max_length=100)
    age = IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'user'
        # verbose_name = 'Userxxx'
        # verbose_name_plural = 'Userxxxs'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]


class Product(Model):
    name = CharField(max_length=100)
    price = IntegerField()
    quantity = IntegerField()
    # slug = CharField(max_length=100, unique=True)
    slug = SlugField()
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'product'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['slug'], name='unique_slug'),
            # models.CheckConstraint(check=models.Q(price__gte=200), name='price_gte_200'),

        ]

class ayoub(models.Model):
    name = CharField(max_length=200)
    class Meta:
        db_table = "ayoub"
        ordering = ['-name']