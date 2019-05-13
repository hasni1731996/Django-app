from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .serializers import *
from django.http import HttpResponse

class User_register(TemplateView):
    template_name = 'login/login.html'

    def post(self, request,*args, **kwargs):
        username =request.POST.get('username')
        password =request.POST.get('pass')
        print(username,password)
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return render(request, 'login/index.html',status=status.HTTP_200_OK)
        return render(request, 'login/login.html', {'data': 'password or username is wrong'},status=status.HTTP_404_NOT_FOUND)

class User_Profile(TemplateView):
    template_name = 'profile/profile.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(request.user.email)
            print('role',request.user.user_name.role)
            return render(request, 'profile/profile.html' ,status=status.HTTP_200_OK)
        return render(request, '400.html' ,status=status.HTTP_200_OK)

class User_Logout(TemplateView):
    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs):
        print('in logout view')
        if request.user.is_authenticated:
            logout(request)
            return render(request, 'login/login.html' ,status=status.HTTP_200_OK)
        return render(request, 'login/login.html' ,status=status.HTTP_200_OK)

    def post(self, request,*args, **kwargs):
        username =request.POST.get('username')
        password =request.POST.get('pass')
        print(username,password)
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return render(request, 'login/index.html',status=status.HTTP_200_OK)
        return render(request, 'login/login.html', {'data': 'password or username is wrong'},status=status.HTTP_404_NOT_FOUND)

class Add_User(TemplateView):
    template_name = 'admin/adduser.html'

    def post(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            try:
                user = User.objects.create_user(
                    username=request.POST.get('username'),
                    email=request.POST.get('email'),
                    password=request.POST.get('pass'),
                    first_name=request.POST.get('first_name'),
                    last_name= request.POST.get('last_name')
                    )
            except:
                return render(request,'admin/adduser.html', status=status.HTTP_400_BAD_REQUEST)

            if user !='':
                email=request.POST.get('email')
                user = User.objects.get(email=request.POST.get('email'))
                _Register = Portal_Management(
                    user=user,
                    cnic_no=request.POST.get('cnic'),
                    phone_no=request.POST.get('mobile'),
                    role=request.POST.get('user_role'),
                    address=request.POST.get('address'),
                    pic=request.POST.get('img')
                    )
                _Register.save()
            else:
                print('in exception')
                return render(request,'admin/adduser.html', status=status.HTTP_400_BAD_REQUEST)

            return render(request, 'admin/adduser.html',status=status.HTTP_200_OK)
        #print(first_name,last_name,cnic,user_role,mobile,email,address,img,username,password)
        return render(request, '400.html' ,status=status.HTTP_200_OK)

class Patient_Registration(TemplateView):
    template_name = 'user/register.html'

    def post(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            Patient_Register.objects.create(
                name= request.POST.get('name'),
                age = request.POST.get('age')
            )
            return render(request, 'user/register.html',status=status.HTTP_200_OK)
        return render(request, '400.html' ,status=status.HTTP_200_OK)

class Patient_view_user(TemplateView):
    template_name = 'user/patients_data.html'

    def get(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            date_current=timezone.localtime(timezone.now()).date()
            allpatients=Patient_Register.objects.filter(created_date=date_current)
            context={
            'allpatients': allpatients
            }
            return render(request, 'user/patients_data.html', context,status=status.HTTP_200_OK)
        return render(request, '400.html' ,status=status.HTTP_200_OK)

@method_decorator(csrf_exempt, name='dispatch')
class Patient_view_admin(TemplateView):
    template_name = 'admin/view_all_patients.html'

    def get(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            allpatients=Patient_Register.objects.all()
            context={
            'allpatients': allpatients
            }
            return render(request, 'admin/view_all_patients.html', context,status=status.HTTP_200_OK)
        return render(request, '400.html' ,status=status.HTTP_200_OK)

    def put(self, request,*args, **kwargs):
        if request.user.is_authenticated and request.is_ajax():
            #print('in put function here... & ajax request',request.body)
            body_data = request.body.decode('utf-8')
            data = json.loads(body_data)
            print(data)
            obj = Patient_Register.objects.get(id=data['id'])
            serializer = Patient_Serializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(request, 'admin/view_all_patients.html',status=status.HTTP_200_OK)
            return render(request, '400.html' ,status=status.HTTP_200_OK)
    
    def delete(self, request,*args, **kwargs):
        if request.user.is_authenticated and request.is_ajax():
            print('in delete Request..')
            body_data = request.body.decode('utf-8')
            data = json.loads(body_data)
            print(data)
            Patient_Register.objects.get(id=data['id']).delete()
            return HttpResponse(request, 'admin/view_all_patients.html',status=status.HTTP_200_OK)
        return render(request, '400.html' ,status=status.HTTP_200_OK)