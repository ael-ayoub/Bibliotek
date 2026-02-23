from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=120)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name