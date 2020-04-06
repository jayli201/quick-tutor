from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import TutorSignup
from django.contrib import messages
from .forms import TutorSignupForm
from students import urls
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth import logout
from students.models import StudentSignup
from django.contrib.auth.models import User

# getting the secret access token from .env file
from dotenv import load_dotenv
load_dotenv()
import os
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

def home(request):
    user = TutorSignup.objects.get(user=request.user)
    status = user.status
    return render(request, 'tutors/home.html', {'ACCESS_TOKEN': ACCESS_TOKEN, 'status': status}) 

def logoutview(request):
    logout(request)
    return redirect('students:landing')

class ProfileView(generic.ListView):
    template_name = 'tutors/profile.html'
    context_object_name = 'profile_list'

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            user = StudentSignup.objects.get(user=self.request.user)
            context['hasother'] = 'yes'
            return context
        except:
            context['hasother'] = 'no'
            return context

    def get_queryset(self):
        try:
            request_user = User.objects.get(username=self.kwargs['username'])
            return TutorSignup.objects.filter(user=request_user)
        
        except:
            return TutorSignup.objects.filter(user=self.request.user)
    

def activate(request):
    if request.method == 'POST':
        longitude = request.POST.get('long_form')
        latitude = request.POST.get('lat_form')
        user = TutorSignup.objects.get(user=request.user)
        user.longitude = longitude
        user.latitude = latitude
        user.status = True
        user.save()
        return HttpResponseRedirect('/tutors/')

def deactivate(request):
    if request.method == 'POST':
        user = TutorSignup.objects.get(user=request.user)
        user.longitude = None
        user.latitude = None
        user.status = False
        user.save()
        return HttpResponseRedirect('/tutors/')

def edit_form(request):
    if request.method == 'POST':
        phone = request.POST['phone_number']
        classes = request.POST['classes']
        subjects = request.POST.get("subjects")  
        pay = request.POST['pay']
        payment_method = request.POST.get("payment_method")  
        user = TutorSignup.objects.get(user=request.user)
        user.phone_number = phone
        user.classes = classes
        user.subjects = subjects
        user.pay = pay
        user.payment_method = payment_method
        user.save()
        return redirect('tutors:myprofile')
    else:
        form = TutorSignupForm()
    return render(request, 'tutors/edit.html', {'form': form})

def signup_form(request):
    if request.method == 'POST':
        form = TutorSignupForm(request.POST)
        try:
            person = TutorSignup.objects.get(user=request.user)
            messages.error(request,'Tutor Account Already Exists For This User!')
            return redirect('/tutors/signup')
        except TutorSignup.DoesNotExist or IntegrityError or MultiValueDictKeyError: 
            if form.is_valid():
                phone = request.POST['phone_number']
                classes = request.POST['classes']
                subjects = request.POST['subjects']            
                pay = request.POST['pay']
                longitude = None
                latitude = None
                status = False
                payment_method = request.POST['payment_method']
                user_object = TutorSignup.objects.create(user=request.user, phone_number = phone, classes = classes, subjects = subjects, pay = pay, payment_method = payment_method, longitude = longitude, latitude = latitude)
                user_object.save()
        return render(request, 'tutors/home.html')

    else:
        form = TutorSignupForm()
    return render(request, 'tutors/signup.html', {'form': form}) 