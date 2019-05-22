from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', User_register.as_view(), name="user_login"), ##### default url when no url is provided#####

    path('profile/', User_Profile.as_view(), name='user_profile'), ######### profile url for both admin/user

    path('logout/', User_Logout.as_view(), name='account_logout'), ######### logout url for both admin/user

    path('adduser/', Add_User.as_view(), name='postuser'), ######## add user by admin

    path('addpatient/', Patient_Registration.as_view(), name='adding_patient'), ####### add patient by user

    path('patients_data/', Patient_view_user.as_view(), name='view_patients'), ## user views patient's details only (today) 

    path('view_patients_data_admin/', Patient_view_admin.as_view(), name='view_patients_admin'), ## admin view details about all patients

    path('dashboard/',Dashboard_User.as_view(), name = 'user_dashboard'), ##### Dashboard url/link for both Admin/user

    path('createuser/', User_create_admin.as_view(), name='admincreate_user'), 

]
