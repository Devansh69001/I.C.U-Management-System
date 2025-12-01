from django.db import models
from patients.models import Patient

class PatientVital(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='vitals')
    date = models.DateField()
    time = models.TimeField(auto_now_add=True)
    bp = models.CharField(max_length=20, blank=True, null=True)
    oxygen = models.CharField(max_length=20, blank=True, null=True)
    pulse = models.IntegerField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-date', '-time']

    def __str__(self):
        return f"{self.patient} - {self.date} {self.bp}/{self.oxygen}"
