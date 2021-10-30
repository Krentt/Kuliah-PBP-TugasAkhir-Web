from django import forms
from .models import ProdukMasker

class ProdukMaskerForm(forms.ModelForm):
    class Meta:
        model = ProdukMasker
        fields = ['nama', 'rating', 'deskripsi', 'harga', 'stok', 'image']
        widgets = {
            'nama' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Masker Karbon Aktif',
                'required' : ''
            }),
            'rating' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : '90 (out of 100)',
                'required' : ''
            }),
            'deskripsi' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Masker wajah ini dapat mengatasi masalah kulit berminyak dan berjerawat',
                'required' : ''
            }),
            'harga' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : '10 (in dollars)',
                'required' : ''
            }),
            'stok' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : '1000',
                'required' : '',
            }),
        }