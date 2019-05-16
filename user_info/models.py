from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from phone_field import PhoneField
from django.utils.safestring import mark_safe
from django.db.models import Count
from datetime import date
from django.utils import timezone
import datetime

def generateUUID():
    return str(uuid4())

class Portal_Management(models.Model):
    USER = 'USER'
    ADMIN = 'ADMIN'
    USER_CHOICES = ((USER, 'user'),(ADMIN, 'admin'))
    id = models.UUIDField(primary_key=True, default=generateUUID, editable=False)
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE,related_name='user_name')
    pic = models.ImageField(blank=True,null=True)
    address = models.CharField(max_length=100)
    phone_no = PhoneField(blank=True, help_text='Contact phone number')
    cnic_no = models.CharField(max_length=200)
    role = models.CharField(max_length=15, choices=USER_CHOICES)
    created_date = models.DateField(default=date.today)

    def image_tag(self):
        if self.pic:
            return mark_safe('<img src="%s" style="width: 40px; height:40px;" />' % self.pic.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.user.username

class Todays_Patients(models.Manager):
    def total_patient_today(self):
        date_current = datetime.datetime.now().date()
        return self.filter(created_date=date_current).aggregate(Count('id' , distinct=True))

class Patient_Register(models.Model):
    id = models.UUIDField(primary_key=True, default=generateUUID, editable=False)
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    created_date = models.DateField(default=date.today)
    objects = models.Manager()
    today_patient = Todays_Patients() ##it returns details of total patients todays & number of patients today

    def __str__(self):
        return "%s (%s)" % (self.name, self.age)