from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from Auth.models import Profile,Store
import string,random
from .models import Bill, ListOfProducts
from Auth.models import Customer
from Products.models import Product


def create_bill(request, *args, **kwargs):
    context = {
        'products': Product.objects.filter(store=request.user.profile.store)
    }
    if request.method == "POST":
        total = 0
        for x in request.POST:
            if x[0] == 'i':
                total = total + Product.objects.get(id=request.POST[x]).price * int(request.POST['q-' + x])
        try:
            cust = Customer.objects.filter(PhoneNumber=request.POST['phonenumber']).first()
            b = Bill(customer=cust,store=request.user.profile.store, total=total)
            b.save()
            for x in request.POST:
                if x[0] == 'i':
                    l = ListOfProducts(product=Product.objects.get(id=request.POST[x]), bill=b,
                                       quantity=request.POST['q-' + x])
                    l.save()
        except:
            cust = Customer.objects.create(PhoneNumber=request.POST['phonenumber'],name=request.POST['name'],store=request.user.profile.store)
            cust.save()
            b = Bill(customer=cust,store=request.user.profile.store, total=total)
            b.save()
            for x in request.POST:
                if x[0] == 'i':
                    l = ListOfProducts(product=Product.objects.get(id=request.POST[x]), bill=b,
                                       quantity=request.POST['q-' + x])
                    l.save()
    return render(request, 'bill.html', context)

def check_cust(request, *args, **kwargs):
    phonenumber = request.GET['phonenumber']
    try:
        cust = Customer.objects.filter(PhoneNumber=phonenumber).first()
        data = {
            'result': 'found',
            'name': cust.name,
        }
    except:
        data = {
            'result': 'not_found'
        }
    return JsonResponse(data)
