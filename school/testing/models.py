from django.db import models
from django.db.models import Model, CharField, IntegerField
# Create your models here.
class Users(Model):
    name = CharField(max_length=120, unique=True)
    age = IntegerField()
    class Meta:
        def __str__(self):
            return f"name: {self.name}, age: {self.age}"
        ordering = ["-age"]