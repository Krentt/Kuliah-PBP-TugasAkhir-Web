from django.core import serializers
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
import json
# Create your views here.
def index(request) :
    return render(request, 'home_page/home.html')
    
