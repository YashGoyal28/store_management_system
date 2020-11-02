from django.shortcuts import render
from .models import Product

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
