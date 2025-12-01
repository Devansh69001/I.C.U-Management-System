from django.contrib import admin
from .models import Patient, VitalReading

'''@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'first_name', 'last_name', 'gender', 'blood_group', 'is_admitted']
    list_filter = ['is_admitted', 'gender', 'blood_group', 'created_at']
    search_fields = ['patient_id', 'first_name', 'last_name', 'phone', 'email']
    fieldsets = (
        ('Personal Information', {'fields': ('patient_id', 'first_name', 'last_name', 'date_of_birth', 'gender')}),
        ('Medical Information', {'fields': ('blood_group', 'allergies', 'medical_history', 'current_medications')}),
        ('Contact Information', {'fields': ('phone', 'email', 'address')}),
        ('Emergency Contact', {'fields': ('emergency_contact', 'emergency_contact_name', 'emergency_contact_relationship')}),
        ('Admission Status', {'fields': ('is_admitted', 'status', 'room_number', 'admission_date', 'discharge_date')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
'''
@admin.register(VitalReading)
class VitalReadingAdmin(admin.ModelAdmin):
    list_display = ['patient', 'timestamp', 'blood_pressure_systolic', 'oxygen_saturation', 'heart_rate', 'temperature']
    list_filter = ['patient', 'timestamp']
    search_fields = ['patient__first_name', 'patient__last_name']