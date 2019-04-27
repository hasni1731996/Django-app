from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

def generateUUID():
    return str(uuid4())

class Portal_Management(models.Model):
    USER = 'USER'
    VENDOR = 'VENDOR'
    USER_CHOICES = ((USER, 'user'),(VENDOR, 'vendor'))
    id = models.UUIDField(primary_key=True, default=generateUUID, editable=False)
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.PROTECT,related_name='user_name')
    pic = models.ImageField(blank=True,null=True)
    address = models.CharField(max_length=100)
    phone_no = models.IntegerField(default=0)
    cnic_no = models.IntegerField(default=0)
    role = models.CharField(max_length=15, choices=USER_CHOICES)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
