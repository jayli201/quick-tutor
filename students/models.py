from django.db import models
from django.conf import settings
from django import forms


class StudentSignup(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, default="")
    classes = models.TextField(max_length=120, default="")

    def __str__(self):
        if self.phone_number==None:
            return "ERROR-NO PHONE NUMBER"
        return self.phone_number