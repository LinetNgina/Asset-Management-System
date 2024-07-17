# dashboard/forms.py

from django import forms
from .models import MaintenanceRecord

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = ['category', 'asset_id', 'comments']