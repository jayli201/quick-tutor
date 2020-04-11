from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import StudentSignup
from tutors.models import TutorSignup, Request
from django.contrib import messages
from .forms import StudentSignupForm
from django.shortcuts import redirect
from django.contrib.auth.models import User

def landing(request):
    if request.user.is_authenticated:
        signed_in = 'yes'
    else:
        signed_in = "no"
    return render(request, 'students/landing.html', {"sign_in":signed_in}) 
    #small change

# getting the secret access token from .env file
from dotenv import load_dotenv
load_dotenv()
import os
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

@login_required(login_url='students:landing')
def home(request):
    tutors = TutorSignup.objects.all()
    active_tutors = []
    tutor_coords = []
    for tutor in tutors:
        if tutor.status == True:
            active_tutors.append(tutor)
    # only passing active tutor info into home template
    for active_tutor in active_tutors:
        longitude = active_tutor.longitude
        tutor_long = float(longitude)
        latitude = active_tutor.latitude
        tutor_lat = float(latitude)
        coords = '{"longitude": tutor_long, "latitude": tutor_lat, "phone": active_tutor.phone_number, "name": active_tutor.user.username}'
        final_coords = eval(coords)
        tutor_coords.append(final_coords)
    return render(request, 'students/home.html', {'ACCESS_TOKEN': ACCESS_TOKEN, 'tutors_list': tutor_coords}) 

def logoutview(request):
    logout(request)
    return redirect('students:landing')

@login_required(login_url='students:landing')
def edit_form(request):
    if request.method == 'POST':
        phone = request.POST['phone_number']
        classes = request.POST['classes']
        user = StudentSignup.objects.get(user=request.user)
        user.phone_number = phone
        user.classes = classes
        user.save()
        return redirect('/students/profile')
    else:
        form = StudentSignupForm()
    return render(request, 'students/edit.html', {'form': form})

@login_required(login_url='students:landing')
def signup_form(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        try:
            user = StudentSignup.objects.get(user=request.user)
            messages.error(request,'Student Account Already Exists For This User!')
            return redirect('/students/signup')
        except StudentSignup.DoesNotExist:
            if form.is_valid():
                phone = request.POST['phone_number']
                classes = request.POST['classes']
                user_object = StudentSignup.objects.create(user=request.user, phone_number = phone, classes = classes)
                user_object.save()
        return render(request, 'students/profile.html')

    else:
        form = StudentSignupForm()
    return render(request, 'students/signup.html', {'form': form}) 

@login_required(login_url='students:landing')    
def search(request):
    return render(request, 'students/search.html')

@login_required(login_url='students:landing')
def choose_signup(request):
    return render(request, 'students/choose.html')

@login_required(login_url='students:landing')
def sign_in_as(request):
    return render(request, 'students/sign_in_as.html')

class ProfileView(LoginRequiredMixin, generic.ListView):
    login_url = 'students:landing'
    redirect_field_name = 'redirect_to'
    template_name = 'students/profile.html'
    context_object_name = 'profile_list'

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            user = TutorSignup.objects.get(user=self.request.user)
            context['hasother'] = 'yes'
            return context
        except:
            context['hasother'] = 'no'
            return context

    def get_queryset(self):
        try:
            request_user = User.objects.get(username=self.kwargs['username'])
            return StudentSignup.objects.filter(user=request_user)
        
        except:
            return StudentSignup.objects.filter(user=self.request.user)

@login_required(login_url='students:landing')
class TutorProfileView(generic.ListView):
    template_name = 'tutors/profile.html'
    context_object_name = 'profile_list'

    def get_queryset(self):
        return StudentSignup.objects.filter(user=self.request.user)

@login_required(login_url='students:landing')
def request_view(request):
    template_name = 'students/requests.html'
    context_object_name = 'requests_list'

    requests = Request.objects.filter(student=request.user)

    return render(request, 'students/requests.html', {'requests_list': requests}) 

@login_required(login_url='students:landing')
def request_close(request):
    if request.method == 'POST':
        request_id = int(request.POST['request_id'])
        specific_request = Request.objects.get(pk=request_id)
        specific_request.delete()
        return HttpResponseRedirect('/students/requests')