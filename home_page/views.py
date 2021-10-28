from django.http.response import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404, render
from home_page.forms import SubscribeForm
from home_page.models import SubscribedEmail
from django.core import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here.
def index(request) :
    return render(request, 'home_page/home.html')


# temp get_image
import re
pattern = re.compile("[^.]*(?<=(.))")
def get_image(request):
    img_list = ['surgical-mask.png', 'n95-mask.png', 'reusable-mask.png', 'plague-mask.png', 'chemical-mask.png']
    if request.is_ajax() and request.method == 'GET':
        request_content = request.GET
        cur_counter = int(request_content["current_counter"])
        path_name = img_list[(cur_counter + 1) % len(img_list)]
        title = re.match(pattern, path_name).group(0)
        path_name = f"static/test_image/{path_name}"
        price = "$10.00"
        data = {
            "src" :path_name,
            "title":title,
            "price":price
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

# @receiver(post_save, sender=Produk)
# def mahasiswa_added(sender, **kwargs) :
#     print(kwargs["instance"].name)