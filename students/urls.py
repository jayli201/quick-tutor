from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('students/', views.home, name='home'),
    path('students/signup', views.signup_form, name='signup_form'),
]