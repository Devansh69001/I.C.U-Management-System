from django import forms
from .models import Prescription, TreatmentPlan

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'medicine_name', 'dosage', 'frequency', 'duration', 'route', 'priority', 'notes']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-select'}),
            'medicine_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicine Name'}),
            'dosage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 500mg'}),
            'frequency': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Twice daily'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 7 days'}),
            'route': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Additional notes'}),
        }

class TreatmentPlanForm(forms.ModelForm):
    class Meta:
        model = TreatmentPlan
        fields = ['patient', 'treatment_type', 'description', 'priority', 'start_date', 'expected_end_date', 'status', 'outcomes']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-select'}),
            'treatment_type': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expected_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'outcomes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
