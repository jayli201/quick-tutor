from django.db import models
from django import forms

class StudentSignup(models.Model):
    phone_num = forms.CharField(required=True)
    classes = forms.CharField(required=True, widget=forms.Textarea)

    def __str__(self):
        return self.phone_num
