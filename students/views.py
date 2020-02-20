from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.shortcuts import render
from .models import StudentSignup
from .forms import StudentSignupForm

def landing(request):
    return render(request, 'students/landing.html') 

def home(request):
    return render(request, 'students/home.html')

def signup_form(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
 
        if form.is_valid():
            phone = request.POST['phone_number']
            classes = request.POST['classes']
            user_object = StudentSignup.objects.create(phone_number = phone, classes = classes)
            user_object.save()
        
        return render(request, 'students/profile.html')

    else:
        form = StudentSignupForm()
    return render(request, 'students/signup.html', {'form': form}) 
    
def search(request):
    return render(request, 'students/search.html')

def profile(request):
    return render(request, 'students/profile.html')
