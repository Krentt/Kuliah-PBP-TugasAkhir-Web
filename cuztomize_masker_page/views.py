from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from cuztomize_masker_page.forms import CustomForm
from django.http.response import HttpResponseRedirect, JsonResponse
from shopping_cart_page.models import *
from cuztomize_masker_page.models import CustomMask 
from django.forms.models import model_to_dict
import cloudinary

# Create your views here.
def custom_mask(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
    form = CustomForm(request.POST or None, request.FILES or None)
    state = ""
    if (form.is_valid() and request.method == 'POST'):
        if ("cart_bt" in request.POST):
            item = form.save()
            item.order = order
            item.save()
            return HttpResponseRedirect('/cart/')   
        elif ("wish_bt" in request.POST):
            form.save()
            return HttpResponseRedirect('/wishlist/')
        elif ("login" in request.POST):
            return HttpResponseRedirect('/login')
        else:
            print("ERROR")
    else :
        if ("login" in request.POST):
            return HttpResponseRedirect('/login')
        elif ("cart_bt" in request.POST):
            state = 'Please fill in all the required fields!'
        elif ("wish_bt" in request.POST):
            state = 'Please fill in all the required fields!'
    return render(request, "custom_page.html", {'form':form, 'state':state})

@csrf_exempt
def update_deskripsi(request):
    data = {
        'SURGICAL' : "Masker bedah atau bisa disebut sebagai masker medis yang biasanya berwarna hijau atau biru. Masker jenis ini mampu menahan droplet sekitar 80-90 persen. Masker ini hanya bisa digunakan satu kali pakai dalam waktu 4 jam pemakaian. Masker ini terutama wajib digunakan oleh pasien sakit dan petugas kesehatan yang tidak menangani pasien COVID-19 secara langsung. Petugas yang menangani pasien COVID-19 secara langsung wajib mengenakan masker N-95 dan APD level 3",
        'SPONGE' : "Familiar dengan masker dengan tipe seperti ini? Kalau kamu suka dengan K-pop Idol, ini adalah masker yang sering dipakai oleh mereka, biasanya untuk menyamar. Nggak sedikit orang yang menjual masker berbahan spons seperti ini di tengah adanya wabah korona ini. Tapi tahu nggak, masker ini nggak didesain untuk menangkal virus, tapi untuk fashion! Masker ini nggak mampu melindungi diri kita dari virus maupun debu. Hanya mampu menahan bakteri maupun pollen sebanyak 5%",
        'PITTA' :  "Masker Pitta Mask, yang sering dikenal sebagai masker K-Pop karena masker ini banyak digunakan oleh para selebriti dari Korea Selatan. Masker ini terbuat dari bahan nano fiber elastis sehingga produk ini mampu melekat sesuai dengan bentuk wajah. Masker ini terdiri dari 1 lapisan yang bisa menahan serbuk sari dan debu. Berbeda dari masker medis, masker ini bisa digunakan kembali dengan mencucinya jika ingin dipakai lagi. Berikut review maskernya.",
        'CLOTH' : "Sering melihat masker-masker beredar yang berbahan kain? Produk ini sebetulnya didesain untuk membuat kita tetap hangat, bukan untuk menahan virus. Mirip dengan Sponge Mask, masker ini nggak mampu menahan virus dan debu. Tapi, mampu menahan bakteri maupun pollen sebanyak 50%. Masker ini sebetulnya masih boleh digunakan oleh kamu yang sehat tapi ada urusan di luar rumah. Tapi, jangan lupa untuk mencuci masker setiap kali setelah pemakaian, dan perhatikan cara melepasnya supaya bagian luar masker nggak terkena wajah kamu.",
    }
    return JsonResponse(data)


@csrf_exempt
def add_custom(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        sex = data["sex"]
        size = data["size"]
        model = data["model"]
        color = data["color"]
        style = data["style"]
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        custom = CustomMask.objects.get_or_create(order=order, sex = sex, size = size, model = model, color = color, style = style)
        dataorder = {}

    else:
        dataorder = {}
       
    
    # print(dataorder)
    return JsonResponse(dataorder, safe=False)