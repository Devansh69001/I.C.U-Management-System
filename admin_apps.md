# ADMIN.PY AND APPS.PY FOR ALL APPS

## staff/admin.py

```python
from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'employee_id', 'specialization', 'department', 'availability_status']
    list_filter = ['role', 'shift', 'department', 'availability_status']
    search_fields = ['user__username', 'employee_id', 'specialization']
    fieldsets = (
        ('User Information', {'fields': ('user', 'role')}),
        ('Employment Details', {'fields': ('employee_id', 'department', 'specialization', 'years_of_experience')}),
        ('Shift & Availability', {'fields': ('shift', 'availability_status')}),
        ('Contact', {'fields': ('phone',)}),
        ('Dates', {'fields': ('date_joined',)}),
    )
    readonly_fields = ['date_joined']
```

## staff/apps.py

```python
from django.apps import AppConfig

class StaffConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staff'
    verbose_name = 'Staff Management'
```

## patients/admin.py

```python
from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'first_name', 'last_name', 'gender', 'blood_group', 'is_admitted']
    list_filter = ['is_admitted', 'gender', 'blood_group', 'created_at']
    search_fields = ['patient_id', 'first_name', 'last_name', 'phone', 'email']
    fieldsets = (
        ('Personal Information', {'fields': ('patient_id', 'first_name', 'last_name', 'date_of_birth', 'gender')}),
        ('Medical Information', {'fields': ('blood_group', 'allergies', 'medical_history')}),
        ('Contact Information', {'fields': ('phone', 'email', 'address')}),
        ('Emergency Contact', {'fields': ('emergency_contact', 'emergency_contact_name')}),
        ('Admission Status', {'fields': ('is_admitted', 'admission_date', 'discharge_date')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
```

## patients/apps.py

```python
from django.apps import AppConfig

class PatientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patients'
    verbose_name = 'Patient Management'
```

## doctor/admin.py

```python
from django.contrib import admin
from .models import Prescription, TreatmentPlan

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['patient', 'medicine_name', 'doctor', 'priority', 'route', 'created_at']
    list_filter = ['priority', 'route', 'created_at']
    search_fields = ['medicine_name', 'patient__patient_id', 'doctor__user__username']
    fieldsets = (
        ('Patient & Doctor', {'fields': ('patient', 'doctor')}),
        ('Medication Details', {'fields': ('medicine_name', 'dosage', 'frequency', 'duration', 'route')}),
        ('Priority & Notes', {'fields': ('priority', 'notes')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'

@admin.register(TreatmentPlan)
class TreatmentPlanAdmin(admin.ModelAdmin):
    list_display = ['patient', 'treatment_type', 'doctor', 'priority', 'status', 'start_date']
    list_filter = ['status', 'priority', 'start_date', 'created_at']
    search_fields = ['treatment_type', 'patient__patient_id', 'doctor__user__username']
    fieldsets = (
        ('Patient & Doctor', {'fields': ('patient', 'doctor')}),
        ('Treatment Details', {'fields': ('treatment_type', 'description', 'start_date', 'expected_end_date')}),
        ('Status & Priority', {'fields': ('priority', 'status')}),
        ('Outcomes', {'fields': ('outcomes',)}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'start_date'
```

## doctor/apps.py

```python
from django.apps import AppConfig

class DoctorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'doctor'
    verbose_name = 'Doctor Services'
```

## nurse/admin.py

```python
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
```

## nurse/apps.py

```python
from django.apps import AppConfig

class NurseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nurse'
    verbose_name = 'Nurse Services'
```

## equipment/admin.py

```python
from django.contrib import admin
from .models import Equipment, MaintenanceLog

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['equipment_id', 'equipment_name', 'location', 'status', 'last_maintenance_date']
    list_filter = ['status', 'equipment_type', 'purchase_date']
    search_fields = ['equipment_id', 'equipment_name', 'location']
    fieldsets = (
        ('Equipment Information', {'fields': ('equipment_id', 'equipment_name', 'equipment_type', 'location')}),
        ('Status', {'fields': ('status',)}),
        ('Dates', {'fields': ('purchase_date', 'warranty_expiry', 'last_maintenance_date', 'next_maintenance_date')}),
        ('Notes', {'fields': ('notes',)}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'purchase_date'

@admin.register(MaintenanceLog)
class MaintenanceLogAdmin(admin.ModelAdmin):
    list_display = ['equipment', 'maintenance_type', 'maintenance_date', 'performed_by', 'cost']
    list_filter = ['maintenance_date', 'maintenance_type']
    search_fields = ['equipment__equipment_name', 'performed_by']
    fieldsets = (
        ('Equipment & Date', {'fields': ('equipment', 'maintenance_date')}),
        ('Maintenance Details', {'fields': ('maintenance_type', 'description', 'performed_by')}),
        ('Cost & Notes', {'fields': ('cost', 'notes')}),
    )
    readonly_fields = ['maintenance_date']
    date_hierarchy = 'maintenance_date'
```

## equipment/apps.py

```python
from django.apps import AppConfig

class EquipmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'equipment'
    verbose_name = 'Equipment Management'
```

## reports/admin.py

```python
from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['patient', 'report_type', 'report_date', 'generated_by', 'created_at']
    list_filter = ['report_type', 'report_date', 'created_at']
    search_fields = ['patient__patient_id', 'generated_by__user__username']
    fieldsets = (
        ('Report Information', {'fields': ('patient', 'report_type', 'report_date', 'generated_by')}),
        ('Content', {'fields': ('summary', 'findings', 'recommendations')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'report_date'
```

## reports/apps.py

```python
from django.apps import AppConfig

class ReportsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reports'
    verbose_name = 'Reports & Analytics'
```

