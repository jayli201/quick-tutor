from django.urls import path
from . import views

app_name = 'tutors'

urlpatterns = [
    path('edit', views.edit_form, name='edit'),
    path('', views.home, name='home'),
    path('logout', views.logoutview, name='logout'),
    path('profile/<str:username>', views.ProfileView.as_view(), name='profile'),
    path('profile', views.ProfileView.as_view(), name='myprofile'),
    path('signup', views.signup_form, name='signup'),
    path('activate', views.activate, name='activate'),
    path('deactivate', views.deactivate, name='deactivate'),
    path('send_request/<str:username>', views.send_request, name='request'),
    path('requests', views.request_view, name='request_view'),
    # path('request_action', views.request_action, name='request_action')
]