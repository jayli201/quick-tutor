from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import TutorSignup, Request
from django.contrib import messages
from .forms import TutorSignupForm
from django.contrib.auth.decorators import login_required
from students import urls
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth import logout
from students.models import StudentSignup
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from uuid import uuid4

# getting the secret access token from .env file
from dotenv import load_dotenv
load_dotenv()
import os
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

@login_required(login_url='students:landing')
def home(request):
    user = TutorSignup.objects.get(user=request.user)
    status = user.status
    latitude = user.latitude
    longitude = user.longitude
    return render(request, 'tutors/home.html', {'ACCESS_TOKEN': ACCESS_TOKEN, 'status': status, 'latitude': latitude, 'longitude': longitude}) 

def logoutview(request):
    logout(request)
    return redirect('students:landing')

class ProfileView(LoginRequiredMixin, generic.ListView):
    login_url = 'students:landing'
    redirect_field_name = 'redirect_to'
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
    
@login_required(login_url='students:landing')
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

@login_required(login_url='students:landing')
def deactivate(request):
    if request.method == 'POST':
        user = TutorSignup.objects.get(user=request.user)
        user.longitude = None
        user.latitude = None
        user.status = False
        user.save()
        return HttpResponseRedirect('/tutors/')

@login_required(login_url='students:landing')
def edit_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone_number']
        classes = request.POST['classes']
        subjects = request.POST.get("subjects")  
        pay = request.POST['pay']
        payment_method = request.POST.get("payment_method")  
        user = TutorSignup.objects.get(user=request.user)
        user.name = name
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

@login_required(login_url='students:landing')
def signup_form(request):
    if request.method == 'POST':
        form = TutorSignupForm(request.POST)
        try:
            person = TutorSignup.objects.get(user=request.user)
            messages.error(request,'Tutor Account Already Exists For This User!')
            return redirect('/tutors/signup')
        except TutorSignup.DoesNotExist or IntegrityError or MultiValueDictKeyError: 
            if form.is_valid():
                name = request.POST['name']
                phone = request.POST['phone_number']
                classes = request.POST['classes']
                subjects = request.POST['subjects']            
                pay = request.POST['pay']
                longitude = None
                latitude = None
                status = False
                payment_method = request.POST['payment_method']
                user_object = TutorSignup.objects.create(user=request.user, name=name, phone_number = phone, classes = classes, subjects = subjects, pay = pay, payment_method = payment_method, longitude = longitude, latitude = latitude)
                user_object.save()
        return render(request, 'tutors/home.html')

    else:
        form = TutorSignupForm()
    return render(request, 'tutors/signup.html', {'form': form}) 

@login_required(login_url='students:landing')
def send_request(request, username):
    # this should be activated when the student clicks the "request" button
    # creates a new instance of a Request

    student = User.objects.get(username=request.user.username)

    request_user = User.objects.get(username=username)
    tutor = User.objects.get(username=username)

    time = datetime.datetime.now()
    r = Request.objects.create(student=student, tutor=tutor, time=time)
    r.save()

    return HttpResponseRedirect(reverse('tutors:myprofile'))

@login_required(login_url='students:landing')
def request_view(request):
    template_name = 'tutors/requests.html'
    context_object_name = 'requests_list'

    requests = Request.objects.filter(tutor=request.user)

    return render(request, 'tutors/requests.html', {'requests_list': requests}) 

@login_required(login_url='students:landing')
def request_action(request):
    if request.method == 'POST':
        request_id = int(request.POST['request_id'])
        action = str(request.POST['action'])
        specific_request = Request.objects.get(pk=request_id)
        specific_request.status = action
        specific_request.save()
        return HttpResponseRedirect('/tutors/requests')

@login_required(login_url='students:landing')
def request_close(request):
    if request.method == 'POST':
        request_id = int(request.POST['request_id'])
        specific_request = Request.objects.get(pk=request_id)
        specific_request.delete()
        return HttpResponseRedirect('/tutors/requests')