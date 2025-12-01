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