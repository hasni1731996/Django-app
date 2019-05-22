from rest_framework import serializers
from .models import *
import base64
import re
from django.core.files.base import ContentFile
import six
import uuid

class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = self.decode_base64(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension
        print('extension..',extension)
        return extension

    def decode_base64(data, altchars=b'+/'):
        data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
        missing_padding = len(data) % 4
        if missing_padding:
            data += b'='* (4 - missing_padding)
        return base64.b64decode(data, altchars)


class Portal_Management_Serializer(serializers.ModelSerializer):
    #pic =  Base64ImageField(max_length=None, use_url=True)
    class Meta:
        model = Portal_Management
        fields= ('pic','address','phone_no','cnic_no','role')

class UserSerializer(serializers.ModelSerializer):
    user_name=Portal_Management_Serializer()
    class Meta:
        model =  User
        fields = ('username','user_name')
        extra_kwargs = {'username': {'validators': [],},}

    def create(self, validated_data):
        user_data = validated_data.pop('user_name')
        user = User.objects.create(**validated_data)
        Portal_Management.objects.create(user=user, **user_data) #####for one to one relation there is no loop here
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