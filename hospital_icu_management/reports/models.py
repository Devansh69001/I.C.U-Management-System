from django.db import models
from patients.models import Patient
from staff.models import Staff

class Report(models.Model):
    REPORT_TYPE_CHOICES = [('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('discharge', 'Discharge')]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reports')
    report_type = models.CharField(max_length=50, choices=REPORT_TYPE_CHOICES)
    generated_by = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    report_date = models.DateField()
    summary = models.TextField()
    findings = models.TextField(blank=True, null=True)
    recommendations = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-report_date']

    def __str__(self):
        return f"{self.report_type.capitalize()} Report: {self.patient.patient_id} - {self.report_date}"