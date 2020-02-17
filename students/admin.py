from django.contrib import admin
 
from .models import StudentSignup
 
 
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'classes')
 
    class Meta:
        model = StudentSignup
 
 
admin.site.register(StudentSignup, FeedbackAdmin)