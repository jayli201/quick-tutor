from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.shortcuts import render
from .models import StudentSignup
from tutors.models import TutorSignup
from .forms import StudentSignupForm
from django.shortcuts import redirect

def landing(request):
    return render(request, 'students/landing.html') 
    #small cgange

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
        coords = '{"longitude": tutor_long, "latitude": tutor_lat, "phone": active_tutor.phone_number}'
        final_coords = eval(coords)
        tutor_coords.append(final_coords)
    return render(request, 'students/home.html', {'ACCESS_TOKEN': ACCESS_TOKEN, 'tutors_list': tutor_coords}) 

def edit_form(request):
    if request.method == 'POST':
        phone = request.POST['phone_number']
        classes = request.POST['classes']
        user = StudentSignup.objects.get(pk=1)
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

class ProfileView(generic.ListView):
    template_name = 'students/profile.html'
    context_object_name = 'profile_list'

    def get_queryset(self):
        return StudentSignup.objects.all()