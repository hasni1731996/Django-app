from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class User_register(TemplateView):
    template_name = 'login/login.html'

    def post(self, request,*args, **kwargs):
        username =request.POST.get('username')
        password =request.POST.get('pass')
        print(username,password)
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return render(request, 'login/index.html', {'username': username},status=status.HTTP_200_OK)
        return render(request, 'login/login.html', {'data': 'password or username is wrong'},status=status.HTTP_404_NOT_FOUND)
        #return render(request, 'login/index.html', {'data': 'password or username is wrong'},status=status.HTTP_404_NOT_FOUND)

class User_Profile(TemplateView):
    template_name = 'login/first.html'