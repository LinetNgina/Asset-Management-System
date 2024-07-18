from django import forms
from .models import MaintenanceRecord

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = ['category', 'asset_id', 'comments', 'return_item']

        widgets = {
            'return_item': forms.RadioSelect(choices=[
                ('yes', 'Yes'),
                ('no', 'No')
            ])
        }
