from django.shortcuts import render

def add_product(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST)
        return render(request, 'add_product.html')
    return render(request, 'add_product.html')
