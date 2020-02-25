from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.shortcuts import render
from .models import TutorSignup
from .forms import TutorSignupForm

def home(request):
    return render(request, 'tutors/home.html') 

class ProfileView(generic.ListView):
    template_name = 'tutors/profile.html'
    context_object_name = 'profile_list'

    def get_queryset(self):
        return TutorSignup.objects.all()

def edit_form(request):
    if request.method == 'POST':
        form = TutorSignupForm(request.POST)
        if form.is_valid():
            phone = request.POST['phone_number']
            classes = request.POST['classes']
            subjects = request.POST['subjects']            
            pay = request.POST['pay']
            payment_method = request.POST['payment_method']

            user = TutorSignup.objects.first()
            user.phone = phone
            user.save()
        
        return render(request, 'tutors/profile.html')

    else:
        form = TutorSignupForm()
    return render(request, 'tutors/profile.html', {'form': form}) 

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