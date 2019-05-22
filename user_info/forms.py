from django import forms

from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Portal_Management
        fields = ('user','pic', 'address','phone_no','cnic_no','role')