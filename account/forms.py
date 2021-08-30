from django import forms
from django.contrib.auth import get_user_model

from .models import StudentProfile

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            "username": forms.TextInput(attrs={'required': True}),
            "first_name": forms.TextInput(attrs={'required': True}),
            "last_name": forms.TextInput(attrs={'required': True}),
            "email": forms.TextInput(attrs={'required': True}),
            "password": forms.PasswordInput(attrs={'required': True}),
        }

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        # fields = "__all__"
        exclude = ['user',]
