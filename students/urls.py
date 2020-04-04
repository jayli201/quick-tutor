from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'students'
urlpatterns = [
    path('', views.landing, name='landing'),
    path('students/edit', views.edit_form, name='student_edit'),
    path('students/', views.home, name='home'),
    path('students/signup', views.signup_form, name='signup_form'),
    path('students/search', views.search, name='search'),
    path('students/profile', views.ProfileView.as_view(), name='profile'),
    path('students/choose', views.choose_signup, name='choose_signup'),
    path('students/signin', views.sign_in_as, name='sign_in_as')
]