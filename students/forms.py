from django import forms
 
from .models import StudentSignup
 
 
class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = StudentSignup
        fields = ('phone_number', 'classes')
        required = ('phone_number', 'classes')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True