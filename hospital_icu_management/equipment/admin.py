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