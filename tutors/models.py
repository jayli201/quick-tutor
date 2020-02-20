from django.db import models
from django import forms

class TutorSignup(models.Model):
    phone_number = models.CharField(max_length=12, default=0)
    classes = models.TextField(max_length=120, default=0)
    subjects = models.TextField(max_length=120, default=0)
    pay = models.CharField(max_length=12, default=0)
    payment_method = models.TextField(max_length=120, default=0)

    def __str__(self):
        if self.phone_number==None:
            return "ERROR-NO PHONE NUMBER"
        return self.phone_number