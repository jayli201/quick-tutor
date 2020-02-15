from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render

def landing(request):
    return render(request, 'students/landing.html') 

def home(request):
    return render(request, 'students/home.html') 