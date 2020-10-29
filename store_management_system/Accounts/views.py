from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from Auth.models import Profile,Store
import string, random

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
        if request.method == "POST":
            username=request.POST.get('username')
            def password(length):
                letters_and_digits = string.ascii_letters + string.digits
                result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
                return result_str
            if username is not None :
                username = username.rstrip()
                if username is not '':
                    new_pass = password(10)
                    new_staff = User.objects.create(username=username, password=new_pass)
                    new_staff.save()
                    print(username, new_pass)
                    context = {
                        'store' : request.user.profile.store
                    }
                    return render(request, 'create_staff.html',context);
            print(request.POST)
        context = {
            'store' : request.user.profile.store
        }
        return render(request, 'create_staff.html',context)
    else:
        raise Http404("Dne")
