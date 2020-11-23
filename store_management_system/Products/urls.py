from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.edit_product),
    path('add/', views.add_product),
    path('<int:id>/', views.edit),
]