from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import TutorSignup
from .forms import TutorSignupForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

# getting the secret access token from .env file
from dotenv import load_dotenv
load_dotenv()
import os
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

def home(request):
    return render(request, 'tutors/home.html', {'ACCESS_TOKEN': ACCESS_TOKEN}) 

class ProfileView(generic.ListView):
    template_name = 'tutors/profile.html'
    context_object_name = 'profile_list'

    def get_queryset(self):
        return TutorSignup.objects.all()

class status(generic.ListView):
    template_name = 'tutors/home.html'
    context_object_name = 'my_profile'

    def get_queryset(self):
        return TutorSignup.objects.first()

def activate(request):
    if request.method == 'POST':
        longitude = request.POST.get('long_form')
        latitude = request.POST.get('lat_form')
        user = TutorSignup.objects.first()
        user.longitude = longitude
        user.latitude = latitude
        user.status = True
        user.save()
        return HttpResponseRedirect('/tutors/')

def edit_form(request):
    if request.method == 'POST':
        phone = request.POST['phone_number']
        classes = request.POST['classes']
        subjects = request.POST.get("subjects")  
        pay = request.POST['pay']
        payment_method = request.POST.get("payment_method")  
        user = TutorSignup.objects.get(pk=1)
        user.phone_number = phone
        user.classes = classes
        user.subjects = subjects
        user.pay = pay
        user.payment_method = payment_method
        user.save()
        return redirect('profile')
    else:
        form = TutorSignupForm()
    return render(request, 'tutors/edit.html', {'form': form})

def signup_form(request):
    if request.method == 'POST':
        form = TutorSignupForm(request.POST)
 
        if form.is_valid():
            phone = request.POST['phone_number']
            classes = request.POST['classes']
            subjects = request.POST['subjects']            
            pay = request.POST['pay']
            payment_method = request.POST['payment_method']
            user_object = TutorSignup.objects.create(phone_number = phone, classes = classes, subjects = subjects, pay = pay, payment_method = payment_method)
            user_object.save()
        
        return render(request, 'tutors/home.html')

    else:
        form = TutorSignupForm()
    return render(request, 'tutors/signup.html', {'form': form}) 