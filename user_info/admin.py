from django.contrib import admin
from .models import *

#admin.site.register(Portal_Management)
class PortalAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'created_date', 'image_tag')

admin.site.register(Portal_Management, PortalAdmin)