from os import stat
from django.http.response import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404, render
from home_page.forms import SubscribeForm
from home_page.models import SubscribedEmail
from django.core import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from product_list_page.models import ProdukMasker
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import threading

# Create your views here.
def index(request) :
    return render(request, 'home_page/home.html')

adder = [1]
def get_image(request):
    if request.is_ajax() and request.method == 'GET':
        request_content = request.GET
        cur_counter = int(request_content["current_counter"]) + adder[0]
        masker = get_object_or_404(ProdukMasker, id=cur_counter)
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
        return HttpResponseNotFound()


# keperluan debug
import json
def get_all_mail(request):
    emails = SubscribedEmail.objects.all()
    data = serializers.serialize('json', emails)
    return HttpResponse(json.dumps(json.loads(data), indent=2), content_type='application/json')


@receiver(post_save, sender=ProdukMasker)
def produk_masker_handler(sender, **produk) :
    def mysender():
        nama_produk = produk["instance"].nama
        deskripsi = produk["instance"].deskripsi
        stok = produk["instance"].stok
        price = produk["instance"].harga
        url_image = produk["instance"].imageURL

        for pk, dest in [(semail['email'], semail['email']) for semail in SubscribedEmail.objects.all().values()]:
            email = EmailMultiAlternatives(
                subject="New Mask is Out !!!",
                body=f"""
                {nama_produk}
                deskripsi: {deskripsi}
                stok: {stok}
                price: {price}
                """,
                from_email= settings.EMAIL_HOST_USER,
                to=[dest],
            )
            html_style = """
            <style>
                h1, h4 {
                    color: black;
                }
            </style>\n
            """

            html_content = f"""
            <h1> {nama_produk} </h1>
            <h4> deskripsi: {deskripsi} </h4>
            <h4> stok:  {stok} <h4>
            <h4> harga: {price} <h4>
            <img src="{url_image}">
            <a href="https://pbp-c07.herokuapp.com/unsubscribe/{pk}">Unsubscribe</a>
            """

            html_content = html_style + html_content
            email.attach_alternative(html_content, 'text/html')
            email.send()

    t = threading.Thread(target=mysender, daemon=True)
    t.start()

def unsubscribe(request, id):
    try:
        subscribe_email = get_object_or_404(SubscribedEmail ,id=id)
        subscribe_email.delete()
        return HttpResponse('You have unsibscrebed', status=200)
    except:
        return HttpResponse('Email not found', status=404)