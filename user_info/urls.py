from django.urls import path
from .views import *

urlpatterns = [
    path('login', User_register.as_view()),

]
