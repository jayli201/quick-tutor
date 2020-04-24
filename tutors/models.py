from django.db import models
from django import forms
from django.conf import settings
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
# from students.models import StudentSignup
from django.utils.translation import gettext as _

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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, default="")
    phone_number = models.CharField(max_length=12, default="")
    classes = models.TextField(max_length=120, default="")
    subjects = models.CharField(max_length=120, choices=SUBJECT_CHOICES, default="")
    pay = models.CharField(max_length=12, default="")
    payment_method = models.CharField(max_length=120, choices=PAY_CHOICES, default="")
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    status = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    num_rates = models.IntegerField(default=0)

    def __str__(self):
        if self.phone_number==None:
            return "ERROR-NO PHONE NUMBER"
        return self.phone_number

class Request(models.Model):
    student = models.ForeignKey(User, related_name='students', on_delete=models.CASCADE)
    tutor = models.ForeignKey(User, related_name='tutors', on_delete=models.CASCADE)
    STATUS = (
       ('accept', _('Accept')),
       ('deny', _('Deny')),
       ('No choice', _('No choice')),
   )
    status = models.CharField(
       max_length=32,
       choices=STATUS,
       default='No choice',
   )
    time = models.DateTimeField('time sent')
     
    def __str__(self):
        return self.status