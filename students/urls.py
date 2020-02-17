from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('students/', views.home, name='home'),
    path('students/signup', views.signup_form, name='signup_form'),
    path('students/search', views.search, name='search'),
    path('students/profile', views.profile, name='profile')
]