from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('students/', views.home, name='home'),
<<<<<<< HEAD
    path('students/signup', views.signup_form, name='signup_form'),
=======
    path('students/search', views.search, name='search'),
    path('students/profile', views.profile, name='profile')
>>>>>>> acc49df368a8a4e06b31aade13a7ac5f8f3598fa
]