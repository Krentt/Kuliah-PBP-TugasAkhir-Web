from django.shortcuts import render

# Create your views here.
def plp(request):
    context = {}
    return render(request, "product_list_page.html")