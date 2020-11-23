from django.shortcuts import render
from .models import Product
from Accounts.models import Bill, ListOfProducts
from Auth.models import Customer

def add_product(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST)
        new_product = Product.objects.create(name=request.POST['name'], 
                                            price=request.POST['price'], 
                                            description=request.POST['description'], 
                                            quantity=request.POST['quantity'], 
                                            store=request.user.profile.store)
        return render(request, 'add_product.html')
    return render(request, 'add_product.html')

def edit_product(request, *args, **kwargs):
    context = {
        'products' : Product.objects.filter(store=request.user.profile.store)
    }
    return render(request, 'edit_product.html', context)

def edit(request, *args, **kwargs):
    id_p = kwargs.get('id')
    p = Product.objects.get(id=id_p)
    if request.method == "POST":
        p.name = request.POST['name']
        p.price = request.POST['price']
        p.description = request.POST['description']
        p.quantity = request.POST['quantity']
        p.save()
    return render(request, "edit.html", context={'p' : p})

def create_bill(request, *args, **kwargs):
    context = {
        'products' : Product.objects.filter(store=request.user.profile.store)
    }
    if request.method == "POST":
        total = 0
        for x in request.POST :
            if x[0] == 'i':
                total = total + Product.objects.get(id=request.POST[x]).price * int(request.POST['q-'+x])
        b = Bill(customer=Customer.objects.get(PhoneNumber=request.POST['phone_no']), store=request.user.profile.store, total=total)
        b.save()
        for x in request.POST :
            if x[0] == 'i':
                l = ListOfProducts(product=Product.objects.get(id=request.POST[x]), bill=b, quantity=request.POST['q-'+x])
                l.save()

    return render(request, 'bill.html', context)
