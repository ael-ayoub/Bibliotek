from rest_framework import serializers
from .models import Post

class post_as_json(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
