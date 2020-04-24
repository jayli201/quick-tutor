from django import forms
 
from .models import TutorSignup
 
 
class TutorSignupForm(forms.ModelForm):
    class Meta:
        model = TutorSignup
        fields = ('name', 'phone_number', 'classes', 'subjects', 'pay', 'payment_method')
        required = ('name', 'phone_number', 'classes', 'subjects', 'pay', 'payment_method')
        labels = {
        "phone_number": "Phone Number",
        "classes": "Classes (ex. CS 3240, CS 2150)",
        "pay": "Pay (in $$)",
        "payment_method": "Payment Method"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True