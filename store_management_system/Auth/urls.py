from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.landingpage, name="landing"),
    path('register/', views.register, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('home/', views.home, name="home"),
    path('staff_info/', views.staff_info),
    path('create_staff/', views.create_staff),
]