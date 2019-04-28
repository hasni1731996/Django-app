from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from phone_field import PhoneField
from django.utils.safestring import mark_safe

def generateUUID():
    return str(uuid4())

class Portal_Management(models.Model):
    USER = 'USER'
    ADMIN = 'ADMIN'
    USER_CHOICES = ((USER, 'user'),(ADMIN, 'admin'))
    id = models.UUIDField(primary_key=True, default=generateUUID, editable=False)
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.PROTECT,related_name='user_name')
    pic = models.ImageField(blank=True,null=True)
    address = models.CharField(max_length=100)
    phone_no = PhoneField(blank=True, help_text='Contact phone number')
    cnic_no = models.CharField(max_length=200)
    role = models.CharField(max_length=15, choices=USER_CHOICES)
    created_date = models.DateTimeField(auto_now=True)

    def image_tag(self):
        if self.pic:
            return mark_safe('<img src="%s" style="width: 40px; height:40px;" />' % self.pic.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.user.username
