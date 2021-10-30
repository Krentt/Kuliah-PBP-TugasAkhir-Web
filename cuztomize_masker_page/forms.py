from django import forms
from django.forms import fields
from django.forms.widgets import FileInput
from .models import CustomMask

class CustomForm (forms.ModelForm):
    class Meta:
        model = CustomMask
        fields = ['sex', 'size', 'model', 'color', 'style']
        
        labels={
            'sex': 'sex',
            'size':'size',
            'model':'model',
            'color':'color',
            'style':'style'
        }
        
