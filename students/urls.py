from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('students/', views.home, name='home'),
    path('students/search', views.search, name='search'),
    path('students/profile', views.profile, name='profile')
]