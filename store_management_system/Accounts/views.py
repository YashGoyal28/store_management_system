from django.shortcuts import render
from django.http import Http404
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
        b = Bill(customer=Customer.objects.get(PhoneNumber=request.POST['phone_no']),
                 store=request.user.profile.store, total=total)
        b.save()
        for x in request.POST:
            if x[0] == 'i':
                l = ListOfProducts(product=Product.objects.get(id=request.POST[x]), bill=b,
                                   quantity=request.POST['q-' + x])
                l.save()

    return render(request, 'bill.html', context)
