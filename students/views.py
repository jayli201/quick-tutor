from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from .forms import StudentSignupForm

def landing(request):
    return render(request, 'students/landing.html') 

def home(request):
    return render(request, 'students/home.html')

def signup_form(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'students/home.html')
    else:
        form = StudentSignupForm()
    return render(request, 'students/signup.html', {'form': form})
    
def search(request):
    return render(request, 'students/search.html')

def profile(request):
    return render(request, 'students/profile.html')
