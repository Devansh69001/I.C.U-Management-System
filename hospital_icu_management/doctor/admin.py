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