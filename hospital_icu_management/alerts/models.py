from django.db import models
from patients.models import Patient

class Alert(models.Model):
    STATUS_CHOICES = [
        ('stable', 'Stable'),
        ('warning', 'Warning'),
        ('critical', 'Critical'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    recovery_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    bp = models.CharField(max_length=8, blank=True)  # e.g., "120/80"
    oxygen = models.IntegerField(blank=True, null=True)
    other_vitals = models.CharField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert: {self.patient} - {self.get_recovery_status_display()}"
