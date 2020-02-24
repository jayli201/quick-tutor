from django import forms
 
from .models import TutorSignup
 
 
class TutorSignupForm(forms.ModelForm):
    class Meta:
        model = TutorSignup
        fields = ('phone_number', 'classes', 'subjects', 'pay', 'payment_method')