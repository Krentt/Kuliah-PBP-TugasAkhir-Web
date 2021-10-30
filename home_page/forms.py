from django import forms
from .models import SubscribedEmail


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribedEmail
        fields = "__all__"