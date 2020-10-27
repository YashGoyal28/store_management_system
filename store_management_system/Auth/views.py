from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect


# Create your views here.

def landingpage(request, *args, **kwargs):
    return render(request,'landing.html')