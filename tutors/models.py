from django.db import models
from django import forms

SUBJECT_CHOICES = (
    ('science','science'),
    ('math', 'math'),
    ('english','english'),
)

PAY_CHOICES = (
    ('venmo', 'venmo'),
    ('cash', 'cash'),
    ('paypal', 'paypal'),
)


class TutorSignup(models.Model):
    phone_number = models.CharField(max_length=12, default="")
    classes = models.TextField(max_length=120, default="")
    subjects = models.CharField(max_length=120, choices=SUBJECT_CHOICES, default="")
    pay = models.CharField(max_length=12, default="")
    payment_method = models.CharField(max_length=120, choices=PAY_CHOICES, default="")

    def __str__(self):
        if self.phone_number==None:
            return "ERROR-NO PHONE NUMBER"
        return self.phone_number