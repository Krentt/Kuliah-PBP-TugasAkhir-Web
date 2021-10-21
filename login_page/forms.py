from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

"""
Referensi : https://dev.to/yahaya_hk/usercreation-form-with-multiple-fields-in-django-ek9
"""

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']