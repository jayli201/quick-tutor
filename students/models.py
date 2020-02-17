from django.db import models
from django import forms

class StudentSignup(models.Model):
    phone_num = models.CharField(max_length=12)
    classes = models.TextField(max_length=120)

    def __str__(self):
        if self.phone_num==None:
            return "ERROR-NO PHONE NUMBER"
        return self.phone_num