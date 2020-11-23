from django.shortcuts import render
from .models import Product


def add_product(request, *args, **kwargs):
    if request.method == "POST":
        print(1)
        print(request.POST)
        new_product = Product.objects.create(name=request.POST['name'], 
                                            price=request.POST['price'], 
                                            description=request.POST['description'], 
                                            quantity=request.POST['quantity'],
                                            image=request.FILES['image'],
                                            store=request.user.profile.store)
        return render(request, 'add_product.html')
    return render(request, 'add_product.html')

def edit_product(request, *args, **kwargs):
    print(1)
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


