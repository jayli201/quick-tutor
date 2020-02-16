from django import forms
 
from .models import StudentSignup
 
 
class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = StudentSignup
        exclude = []