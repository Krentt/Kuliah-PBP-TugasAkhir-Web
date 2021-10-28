from django import forms
from django.forms import fields
from .models import CustomMask

class CustomForm (forms.ModelForm):
    class Meta:
        model = CustomMask
        fields = "__all__"


