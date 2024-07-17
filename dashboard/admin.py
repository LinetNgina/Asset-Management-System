# dashboard/admin.py

from django.contrib import admin
from .models import MaintenanceRequest, MaintenanceRecord

admin.site.register(MaintenanceRequest)
admin.site.register(MaintenanceRecord)
