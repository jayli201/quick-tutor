from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render

def home(request):
    return render(request, 'tutors/home.html')