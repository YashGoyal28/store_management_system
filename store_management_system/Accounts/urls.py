from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('staff_info/', views.staff_info),
    path('create_staff/', views.create_staff)
]