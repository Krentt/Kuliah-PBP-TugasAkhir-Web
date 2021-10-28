from django import forms
from .models import ProdukMasker

class ProdukMaskerForm(forms.ModelForm):
    class Meta:
        model = ProdukMasker
        fields = "__all__"