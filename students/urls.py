from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'students'
urlpatterns = [
    path('', views.landing, name='landing'),
    path('students/rating', views.rating, name='ratings'),
    path('students/edit', views.edit_form, name='student_edit'),
    path('students/logout', views.logoutview, name='logout'),
    path('students/', views.home, name='home'),
    path('students/signup', views.signup_form, name='signup_form'),
    path('students/profile', views.ProfileView.as_view(), name='profile'),
    path('students/choose', views.choose_signup, name='choose_signup'),
    path('students/signin', views.sign_in_as, name='sign_in_as'),
    path('students/requests', views.request_view, name='request_view'),
    path('students/profile/<str:username>', views.ProfileView.as_view(), name='profile'),
    path('students/request_close/', views.request_close, name='request_close')
]