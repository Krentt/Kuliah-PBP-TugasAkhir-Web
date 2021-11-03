from django.http.response import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404, render
from home_page.forms import SubscribeForm
from home_page.models import SubscribedEmail
from django.core import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from product_list_page.models import ProdukMasker

# Create your views here.
def index(request) :
    return render(request, 'home_page/home.html')


def get_image(request):
    if request.method == 'GET':
        request_content = request.GET
        cur_counter = int(request_content["current_counter"]) + 1
        masker = get_object_or_404(ProdukMasker, id=cur_counter)
        print(masker.imageURL)
        data = {
            "src" : masker.imageURL,
            "title":masker.nama,
            "price":"$" + str(masker.harga)
        }
        return JsonResponse(data, status=200)
    else:
        return HttpResponseNotFound()    


def subscribe(request):
    if request.is_ajax() and request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Thank You"}, status=200)
        else:
            return JsonResponse({"message": "duplicate"}, status=200)
    else:
        return JsonResponse({"message": "Error"}, status=400)    


# keperluan debug
import json
def get_all_mail(request):
    emails = SubscribedEmail.objects.all()
    data = serializers.serialize('json', emails)
    return HttpResponse(json.dumps(json.loads(data), indent=2), content_type='application/json')

@receiver(post_save, sender=ProdukMasker)
def produk_masker_handler(sender, **kwargs) :
    print(kwargs["instance"].nama)