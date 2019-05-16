from rest_framework import serializers
from .models import *

class Portal_Management_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Portal_Management
        fields= ('pic','address','phone_no','cnic_no','role')

class UserSerializer(serializers.ModelSerializer):
    user_name=Portal_Management_Serializer()
    class Meta:
        model =  User
        fields = ('username' , 'email','user_name')
        extra_kwargs = {'username': {'validators': [],},}

    def create(self, validated_data):
        state_data = validated_data.pop('user_name')
        user = User.objects.create(**validated_data)
        for data_state in state_data:
            Portal_Management.objects.create(user=user, **data_state)
        return user

    def update(self, instance, validated_data):
        states_data = validated_data.pop('user_name')
        real_data = (instance.user_name).all()
        real_data = list(real_data)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        for data in states_data:
            album = real_data.pop(0)
            album.zip = data.get('zip', album.zip)
            album.city = data.get('city', album.city)
            album.save()
        return instance

class Patient_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Patient_Register
        fields= ('name','age','created_date')