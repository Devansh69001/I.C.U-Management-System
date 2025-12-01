from django.db import models
from patients.models import Patient
from staff.models import Staff


class Admission(models.Model):
    ADMISSION_TYPE_CHOICES = [('emergency', 'Emergency'), ('scheduled', 'Scheduled'), ('transfer', 'Transfer')]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='admissions')
    nurse = models.ForeignKey(Staff, limit_choices_to={'role': 'nurse'}, on_delete=models.CASCADE)
    admission_type = models.CharField(max_length=50, choices=ADMISSION_TYPE_CHOICES)
    admission_date_time = models.DateTimeField()
    room_number = models.CharField(max_length=20)
    bed_number = models.CharField(max_length=20)
    chief_complaint = models.TextField()
    vital_signs_bp = models.CharField(max_length=20, blank=True)
    vital_signs_hr = models.IntegerField(blank=True, null=True)
    vital_signs_temperature = models.FloatField(blank=True, null=True)
    vital_signs_rr = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-admission_date_time']

    def __str__(self):
        return f"Admission: {self.patient.patient_id} - {self.admission_date_time.date()}"


class PatientObservation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='observations')
    nurse = models.ForeignKey(Staff, limit_choices_to={'role': 'nurse'}, on_delete=models.CASCADE)
    observation_date_time = models.DateTimeField(auto_now_add=True)
    bp = models.CharField(max_length=20, blank=True)
    heart_rate = models.IntegerField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    respiratory_rate = models.IntegerField(blank=True, null=True)
    oxygen_saturation = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-observation_date_time']

    def __str__(self):
        return f"Observation: {self.patient.patient_id} - {self.observation_date_time}"
