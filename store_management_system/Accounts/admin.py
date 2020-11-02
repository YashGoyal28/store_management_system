from django.contrib import admin
from .models import ListOfProducts, Bill

admin.site.register(Bill)
admin.site.register(ListOfProducts)
