import datetime
from django import template
from user_info.models import *
register = template.Library()
import datetime

################## Get Total Number of Patients according to current date for normal User #################
@register.simple_tag
def patients_objs():
    res=Patient_Register.today_patient.total_patient_today()
    patients=res.get('id__count')
    return patients

################### ENDS ###########################

################## Use Current Date According to the AM/PM ##############
@register.simple_tag
def todays_date():
    return datetime.datetime.now().date()

################# ENds######################################

################## Get All Patients for Admin ###########
@register.simple_tag
def total_patients_objs():
    res = Patient_Register.objects.all()
    return len(res)
################# Ends ################