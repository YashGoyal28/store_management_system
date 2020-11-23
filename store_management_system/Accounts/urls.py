from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('bill/create/', views.create_bill),
    path('check_cust/', views.check_cust),
]