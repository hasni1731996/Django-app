from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView,View,CreateView
from django.shortcuts import render,redirect
from rest_framework import status,generics
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .serializers import *
from django.http import HttpResponse
from collections import OrderedDict
from .fusioncharts import FusionCharts
from .decorators import *
from rest_framework.parsers import MultiPartParser
from .forms import *
from django.urls import reverse_lazy

class User_register(TemplateView):
    template_name = 'login/login.html'

    def post(self, request,*args, **kwargs):
        username =request.POST.get('username')
        password =request.POST.get('pass')
        print(username,password)
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        return render(request, 'login/login.html', {'data': 'password or username is wrong'},status=status.HTTP_404_NOT_FOUND)

@method_decorator(check_user, name='dispatch')
class User_Profile(TemplateView):
    template_name = 'profile/profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'profile/profile.html' ,status=status.HTTP_200_OK)

class User_Logout(TemplateView):
    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs):
        print('in logout view')
        logout(request)
        return render(request, 'login/login.html' ,status=status.HTTP_200_OK)

    def post(self, request,*args, **kwargs):
        username =request.POST.get('username')
        password =request.POST.get('pass')
        print(username,password)
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        return render(request, 'login/login.html', {'data': 'password or username is wrong'},status=status.HTTP_404_NOT_FOUND)


@method_decorator(check_user, name='dispatch')
class Add_User(TemplateView):
    template_name = 'admin/adduser.html'

    def post(self, request,*args, **kwargs):
        data={
            "username":request.POST.get('username'),
            "password":request.POST.get('password2'),
            "user_name":
            {
                "cnic_no":request.POST.get('cnic'),
                "phone_no":request.POST.get('mobile'),
                "role":request.POST.get('user_role'),
                "address":request.POST.get('address'),
                "pic":request.FILES.get('myfile')
            }
        }

        print('files..........',data)
        serializer = UserSerializer(data=data)
        try:
            if serializer.is_valid():
                serializer.save()
                context={'user_created':True}
                return render(request, 'admin/adduser.html',context ,status=status.HTTP_200_OK)
        except:
            print(serializer.errors)
            return render(request, 'admin/adduser.html', status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(check_user, name='dispatch')
class Patient_Registration(TemplateView):
    template_name = 'user/register.html'

    def post(self, request,*args, **kwargs):
        body_data = request.body.decode('utf-8')
        data = json.loads(body_data)
        print('actual data...',data)
        serializer = Patient_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('Success',status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
        return HttpResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@method_decorator(check_user, name='dispatch')
class Patient_view_user(TemplateView):
    template_name = 'user/patients_data.html'

    def get(self, request,*args, **kwargs):
        date_current=timezone.localtime(timezone.now()).date()
        allpatients=Patient_Register.objects.filter(created_date=date_current)
        context={
        'allpatients': allpatients
        }
        return render(request, 'user/patients_data.html', context,status=status.HTTP_200_OK)

@method_decorator(check_user, name='dispatch')
class Dashboard_User(TemplateView):
    template_name = 'login/index.html'

    def get(self, request, *args,**kwrgs):
        response_chart=Patients_Chart()
            ########## Sending Graph Values As Admin login ####
        return render(request, 'login/index.html', { 'output': response_chart.render()}, status=status.HTTP_200_OK)
            ######## Ends ################

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(check_user, name='dispatch')  ####### Two decorators 1st for csrf_exempt 2nd for checking User authentication
class Patient_view_admin(TemplateView):
    template_name = 'admin/view_all_patients.html'

    def get(self, request,*args, **kwargs):
        allpatients=Patient_Register.objects.all()
        context={
        'allpatients': allpatients
        }
        return render(request, 'admin/view_all_patients.html', context,status=status.HTTP_200_OK)

    def put(self, request,*args, **kwargs):
        body_data = request.body.decode('utf-8')
        data = json.loads(body_data)
        print(data)
        obj = Patient_Register.objects.get(id=data['id'])
        serializer = Patient_Serializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('Success',status=status.HTTP_200_OK)
    
    def delete(self, request,*args, **kwargs):
        print('in delete Request..')
        body_data = request.body.decode('utf-8')
        data = json.loads(body_data)
        print(data)
        Patient_Register.objects.get(id=data['id']).delete()
        return HttpResponse('Success',status=status.HTTP_200_OK)

########## Function For Creating Graph & Return Values ##############
def Patients_Chart():
    dataSource = OrderedDict()
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Patients Within Current Year"
    chartConfig["subCaption"] = "With Respect to Per Patients Per Year"
    chartConfig["xAxisName"] = "Months"
    chartConfig["yAxisName"] = "Total Number Of Patients"
    chartConfig["theme"] = "candy"
    chartData = OrderedDict()
    chartData["Jan"] = 20
    chartData["Feb"] = 20
    chartData["Mar"] = 180
    chartData["Apr"] = 140
    chartData["May"] = 115
    chartData["Jun"] = 100
    chartData["Jul"] = 30
    chartData["Aug"] = 30
    chartData["Sep"] = 30
    chartData["Oct"] = 30
    chartData["Nov"] = 30
    chartData["Dec"] = 30
    dataSource["chart"] = chartConfig
    dataSource["data"] = []
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)
    column2D = FusionCharts("column2d", "Patients_Chart", "600", "400", "Patientstchart-container", "json", dataSource)
    return column2D

####################ENDS HERE#############################


class User_create_admin(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser,)