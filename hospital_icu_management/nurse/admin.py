from django.contrib import admin
from .models import Admission, PatientObservation

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['patient', 'admission_type', 'room_number', 'nurse', 'admission_date_time']
    list_filter = ['admission_type', 'admission_date_time']
    search_fields = ['patient__patient_id', 'room_number', 'nurse__user__username']
    fieldsets = (
        ('Patient & Nurse', {'fields': ('patient', 'nurse')}),
        ('Admission Details', {'fields': ('admission_type', 'admission_date_time', 'room_number', 'bed_number')}),
        ('Chief Complaint', {'fields': ('chief_complaint',)}),
        ('Vital Signs', {'fields': ('vital_signs_bp', 'vital_signs_hr', 'vital_signs_temperature', 'vital_signs_rr')}),
        ('Notes', {'fields': ('notes',)}),
    )
    readonly_fields = ['created_at']
    date_hierarchy = 'admission_date_time'

@admin.register(PatientObservation)
class PatientObservationAdmin(admin.ModelAdmin):
    list_display = ['patient', 'nurse', 'observation_date_time', 'heart_rate', 'temperature']
    list_filter = ['observation_date_time', 'nurse']
    search_fields = ['patient__patient_id', 'nurse__user__username']
    fieldsets = (
        ('Patient & Nurse', {'fields': ('patient', 'nurse')}),
        ('Observation Date', {'fields': ('observation_date_time',)}),
        ('Vital Signs', {'fields': ('bp', 'heart_rate', 'temperature', 'respiratory_rate', 'oxygen_saturation')}),
        ('Notes', {'fields': ('notes',)}),
    )
    readonly_fields = ['observation_date_time']
    date_hierarchy = 'observation_date_time'