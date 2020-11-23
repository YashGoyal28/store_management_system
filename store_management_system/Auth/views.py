import string,random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from .models import Store, Profile, Customer


# Create your views here.

def landingpage(request, *args, **kwargs):
    return render(request, 'landing.html')

def home(request, *args, **kwargs):
    if request.user.is_authenticated:
        return render(request, 'base.html')
    return redirect(reverse("landing"))

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
            store=new_store,
            PhoneNumber=phonenumber
        )
        login(request, user)
        data = {
            'result': 'success',
        }
        return JsonResponse(data)


def login_user(request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.profile.role != role:
                data = {
                    'result': 'error',
                }
                return JsonResponse(data)
            login(request, user)
            data = {
                'result': 'success',
            }
            return JsonResponse(data)
        data = {
            'result': 'error',
        }
        return JsonResponse(data)

def logout_user(request, *args, **kwargs):
    logout(request)
    return redirect(reverse('landing'))


def staff_info(request, *args, **kwargs):
    if request.user.profile.role == "Manager":
        context = {
            'staff' : Profile.objects.filter(store=request.user.profile.store).filter(role="Employee")
        }
        return render(request, 'staff_info.html',context);
    else:
        raise Http404("Dne")

def create_staff(request, *args, **kwargs):
    if request.user.profile.role == "Manager":
        context = {
            'store': request.user.profile.store,
            'id': Profile.objects.filter(store=request.user.profile.store).count()
        }
        if request.method == "POST":
            username = request.POST.get('username')
            def password(length):
                letters_and_digits = string.ascii_letters + string.digits
                result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
                return result_str
            if username is not None:
                username = username.rstrip()
                if username != '':
                    new_pass = password(10)
                    new_staff = User.objects.create(username=username, password=new_pass)
                    new_staff.save()
                    new_profile = Profile.objects.create(user=new_staff, role="Employee", store=request.user.profile.store)
                    print(username, new_pass)
                    return render(request, 'create_staff.html', context)
            print(request.POST)
        return render(request, 'create_staff.html', context)
    else:
        raise Http404("Dne")
