from django.forms import ModelForm, TextInput
from .models import Order

class NoteForm(ModelForm):
    class Meta:
        model = Order
        fields = ['note']
        widgets = {
            'note' : TextInput(attrs={'class': 'form-control', 'style':'flex:8', 'placeholder':'Tuliskan catatan pemesanan disini'}),
        }