from django.http.response import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages

"""
Referensi : https://www.ordinarycoders.com/blog/article/django-user-register-login-logout
"""

# Create your views here.
def register_user(request):
    if (request.method == 'POST'):
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            form.save()
            messages.success(request, 'Registration Successful!')
            return HttpResponseRedirect('login')

        messages.error(request, 'Unsuccessful Registration. Invalid Information')
    
    form = RegisterForm()
    context = {'form' : form}
    return render(request, 'login_page/register.html', context)

def login_user(request):
    if (request.method == 'POST'):
        form = AuthenticationForm(data=request.POST)
        if (form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if (user is not None):
                login(request, user)
                messages.success(request, 'Login successful!')
                return HttpResponseRedirect('home-page')
        
        messages.error(request, 'Invalid username or password')

    form = AuthenticationForm()
    context = {'form' : form}
    return render(request, 'login_page/login.html', context)

def logout_user(request):
    logout(request)
    messages.info(request, 'Successfully logged out')
    return HttpResponseRedirect('home-page')

def home_page(request):
    return render(request, 'home_page/home.html')
