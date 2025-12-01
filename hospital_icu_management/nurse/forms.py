from django import forms
from .models import Admission, PatientObservation

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['patient', 'admission_type', 'admission_date_time', 'room_number', 
                  'bed_number', 'chief_complaint', 'vital_signs_bp', 'vital_signs_hr',
                  'vital_signs_temperature', 'vital_signs_rr', 'notes']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-select'}),
            'admission_type': forms.Select(attrs={'class': 'form-select'}),
            'admission_date_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
            'bed_number': forms.TextInput(attrs={'class': 'form-control'}),
            'chief_complaint': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'vital_signs_bp': forms.TextInput(attrs={'class': 'form-control'}),
            'vital_signs_hr': forms.NumberInput(attrs={'class': 'form-control'}),
            'vital_signs_temperature': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'vital_signs_rr': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PatientObservationForm(forms.ModelForm):
    class Meta:
        model = PatientObservation
        fields = ['patient', 'bp', 'heart_rate', 'temperature', 'respiratory_rate', 'oxygen_saturation', 'notes']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-select'}),
            'bp': forms.TextInput(attrs={'class': 'form-control'}),
            'heart_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'temperature': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'respiratory_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'oxygen_saturation': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
