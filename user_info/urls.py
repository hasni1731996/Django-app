from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', User_register.as_view()),

    path('profile/', User_Profile.as_view(), name='user_profile'),
]
