from django.shortcuts import render

from cuztomize_masker_page.forms import CustomForm
from django.http.response import HttpResponseRedirect

# Create your views here.
def custom_mask(request):
    form = CustomForm(request.POST, request.FILES)
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/shopping-cart-page/')
    else :
        return render(request, "custom_page.html", {'form':form})