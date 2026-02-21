from django import forms
# from django.forms.models import user

class login_info(forms.Form):
    username = forms.CharField(max_length=222, required=True)
    email = forms.CharField( max_length=222, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

# class Post(forms.Form):
