from django import forms
 
from .models import TutorSignup
 
 
class TutorSignupForm(forms.ModelForm):
    class Meta:
        model = TutorSignup
        fields = ('phone_number', 'classes', 'subjects', 'pay', 'payment_method')
        required = ('phone_number', 'classes', 'subjects', 'pay', 'payment_method')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True