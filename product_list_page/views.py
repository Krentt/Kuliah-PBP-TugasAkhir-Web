from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .forms import ProdukMaskerForm
from .models import ProdukMasker
from django.contrib.auth.decorators import login_required


# Create your views here.
def plp(request):
    product = ProdukMasker.objects.all()
    response = {'product': product}
    return render(request, 'product_list_page.html', response)

@login_required(login_url="/admin/login/")
def add_mask(request):
    if request.method == 'POST':
        form = ProdukMaskerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/product_list_page/')
    else:
        form = ProdukMaskerForm()
    return render(request, 'product_form.html', {'form': form})