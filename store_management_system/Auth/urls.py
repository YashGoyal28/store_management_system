from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.landingpage, name="landing"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_user, name="logout"),
    path('home/', views.home, name="home")
]