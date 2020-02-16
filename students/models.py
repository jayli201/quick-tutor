from django.db import models
from django import forms

class StudentSignupForm(forms.Form):
    phone_num = forms.CharField(required=True)
    classes = forms.CharField(required=True, widget=forms.Textarea)