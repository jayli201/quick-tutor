from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render


def landing(request):
    return HttpResponse("Hello, world. You're at the Quick Tutor home page.")


def home(request):
    return HttpResponse("Hello, world. You're at the students home page.")
