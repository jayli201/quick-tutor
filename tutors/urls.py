from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    path('', views.profile, name='profile'),
=======
    path('profile', views.profile, name='profile')
>>>>>>> 9b41ccd3f733a61b3cbcfaf4c7819bd3e52d07df
]