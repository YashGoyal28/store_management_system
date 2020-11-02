from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from Auth.models import Store
from Products.models import Product
from Auth.models import Customer

class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.FloatField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


class ListOfProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)