from django import forms
from .models import Equipment

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = [
            'equipment_id',
            'equipment_name',
            'equipment_type',
            'category',
            'serial_number',
            'location',
            'status',
            'purchase_date',
            'warranty_expiry',
            'last_maintenance_date',
            'next_maintenance_date',
            'notes',
        ]
        widgets = {
            'equipment_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Equipment Name'}),
            'equipment_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Equipment Type'}),
            'equipment_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Equipment ID'}),
            "purchase_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'last_maintenance_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_maintenance_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Additional notes'}),
        }
