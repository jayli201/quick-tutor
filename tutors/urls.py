from django.urls import path

from . import views

urlpatterns = [
    path('edit', views.edit_form, name='edit'),
    path('', views.home, name='home'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('signup', views.signup_form, name='signup'),
    path('activate', views.activate, name='activate'),
    path('deactivate', views.deactivate, name='deactivate')
]