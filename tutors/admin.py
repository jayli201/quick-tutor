from django.contrib import admin
 
from .models import TutorSignup, Request
 
 
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'classes', 'subjects', 'pay', 'payment_method')
 
    class Meta:
        model = TutorSignup
 
 
admin.site.register(TutorSignup)
admin.site.register(Request)