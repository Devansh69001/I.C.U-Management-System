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