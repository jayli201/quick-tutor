from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import logout
from .models import StudentSignup
from tutors.models import TutorSignup
from django.contrib import messages
from .forms import StudentSignupForm
from django.shortcuts import redirect

def landing(request):
    return render(request, 'students/landing.html') 
    #small change

# getting the secret access token from .env file
from dotenv import load_dotenv
load_dotenv()
import os
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

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
    
def search(request):
    return render(request, 'students/search.html')

def choose_signup(request):
    return render(request, 'students/choose.html')

class ProfileView(generic.ListView):
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
        return StudentSignup.objects.filter(user=self.request.user)

class TutorProfileView(generic.ListView):
    template_name = 'tutors/profile.html'
    context_object_name = 'profile_list'

    def get_queryset(self):
        return StudentSignup.objects.filter(user=self.request.user)