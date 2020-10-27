from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save

role_choices = (
    ('Manager', 'Manager'),
    ('Employee', 'Employee'),
)

class Store(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=role_choices, default='Employee')
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Customer(models.Model):
    name = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=10)
    last_visited = models.DateField(auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

