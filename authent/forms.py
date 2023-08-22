from django import forms
from django.contrib.auth.forms import UserCreationForm
from authent.models import User

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
       
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            "username": "Username",
            "email" : "Email Address",
            "password1":"password",
            "password2":"Confirm Password"
        }

        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:outline-none focus:ring-4 focus:ring-blue-200', }),
            "email": forms.EmailInput(attrs={'class': 'px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:outline-none focus:ring-4 focus:ring-blue-200 form-control', "type":'email','required':'true'}),
            "password1": forms.PasswordInput(attrs={'class': 'px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:outline-none focus:ring-4 focus:ring-blue-200', 'type':'password1','id':'pass1'}),
            "password2": forms.PasswordInput(attrs={'class': 'px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:outline-none focus:ring-4 focus:ring-blue-200', 'type':'password2', 'id':'pass2'}),
        }