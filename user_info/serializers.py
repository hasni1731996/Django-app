from rest_framework import serializers
from .models import *

class Patient_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Patient_Register
        fields= ('name','age','created_date')