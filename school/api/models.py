from django.db import models
from django.contrib import admin


# @admin.register(Post)
class Post(models.Model):
    title  = models.CharField(max_length=100)
    content = models.CharField(max_length=300)

    class Meta:
        db_table = "Post"

class Comments(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)