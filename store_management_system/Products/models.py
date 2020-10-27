from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from Auth.models import Store

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField(default='')
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to="product/", default="/product/default.jpg")
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    def __str__(self):
        return self.name