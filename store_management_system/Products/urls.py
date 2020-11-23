from django.urls import path,include
from . import views

urlpatterns = [
    path('add/', views.add_product),
    path('edit/', views.edit_product),
    path('edit/<int:id>/', views.edit),
    path('bill/create/', views.create_bill),
]