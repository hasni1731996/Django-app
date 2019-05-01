from django.contrib import admin
from .models import *

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'created_date')
admin.site.register(Patient_Register,PatientAdmin)

class PortalAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'created_date', 'image_tag')

admin.site.register(Portal_Management, PortalAdmin)