from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from .models import UserForm

"""
Referensi : 
- https://dev.to/yahaya_hk/usercreation-form-with-multiple-fields-in-django-ek9
- https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa
"""

class RegisterForm(ModelForm):

    class Meta:
        model = UserForm
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'confirm_password']
        widgets = {
            'first_name' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Ricardo',
                'required' : ''
            }),
            'last_name' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Milos',
                'required' : ''
            }),
            'email' : EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'ricardo@gmail.com',
                'required' : ''
            }),
            'username' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'ricardo_milos',
                'required' : ''
            }),
            'password' : PasswordInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter password',
                'required' : '',
                'minlength' : '8'
            }),
            'confirm_password' : PasswordInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter confirmation password',
                'required' : '',
            })
        }
