from django.http import HttpResponse
<<<<<<< HEAD
from polls.forms import SuggestionsForm
=======
from django.views import generic
from django.shortcuts import render
>>>>>>> ea9cf5005f87d80f5e3c06aa9033d56ed874d21b

def landing(request):
    return render(request, 'students/landing.html') 

def home(request):
    return render(request, 'students/home.html') 