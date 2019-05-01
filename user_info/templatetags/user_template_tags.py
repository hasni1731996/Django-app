import datetime
from django import template
from user_info.models import *
register = template.Library()

################## Get Total Number of Patients according to current date for normal User #################
@register.simple_tag
def patients_objs():
    res=Patient_Register.today_patient.total_patient_obj()
    patients=res.get('id__count')
    return patients

################### ENDS ###########################

################## Get All Patients for Admin ###########
@register.simple_tag
def total_patients_objs():
    res = Patient_Register.objects.all()
    return len(res)
################# Ends ################