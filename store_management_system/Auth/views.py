from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Store, Profile, Customer


# Create your views here.

def landingpage(request, *args, **kwargs):
    return render(request, 'landing.html')

def home(request, *args, **kwargs):
    return render(request, 'base.html')

def register(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        store = request.POST['store']
        address = request.POST['address']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if len(username) > 50:
            data = {
                'result': 'error',
                'target': 'username',
                'message': 'Username had a length limitation of 20 characters',
            }
            return JsonResponse(data)
        if User.objects.filter(username=username).exists() == True:
            data = {
                'result': 'error',
                'target': 'username',
                'message': 'Username already taken',
            }
            return JsonResponse(data)
        if len(store) > 200:
            data = {
                'result': 'error',
                'target': 'store',
                'message': 'Store name had a length limitation of 200 characters',
            }
            return JsonResponse(data)
        if len(address) > 500:
            data = {
                'result': 'error',
                'target': 'store',
                'message': 'Store address had a length limitation of 200 characters',
            }
            return JsonResponse(data)
        if password2 != password1:
            data = {
                'result': 'error',
                'target': 'password',
                'message': 'Your password didn\'t match',
            }
            return JsonResponse(data)
        if len(password1) < 8:
            data = {
                'result': 'error',
                'target': 'password',
                'message': 'Password must contain atleast 8 characters',
            }
            return JsonResponse(data)

        user = User.objects.create_user(username, email, password1)
        user = authenticate(request, username=username, password=password1)
        new_store = Store.objects.create(
            name=store,
            address=address
        )
        profile = Profile.objects.create(
            user=user,
            role="Manager",
            store=new_store
        )
        login(request, user)
        data = {
            'result': 'success',
        }
        return JsonResponse(data)


def logout_user(request, *args, **kwargs):
    logout(request)
    return redirect(reverse('landing'))