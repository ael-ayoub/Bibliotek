# from django.forms import Form
from django import forms
from .models import Post, Comments
# from .models import etudian

# class etudianForm(forms.ModelForm):
#     class Meta:
#         model = etudian
#         fields = {"name", "age", "email"}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = {"title", "content"}

class ComentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = {"post_id", "content"}