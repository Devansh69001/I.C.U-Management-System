from django.db import models
from patients.models import Patient
from staff.models import Staff

class Prescription(models.Model):
    PRIORITY_CHOICES = [('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Urgent', 'Urgent')]
    ROUTE_CHOICES = [
        ('oral', 'Oral'),
        ('intravenous', 'Intravenous'),
        ('intramuscular', 'Intramuscular'),
        ('topical', 'Topical')
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Staff, limit_choices_to={'role': 'doctor'}, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=50)
    duration = models.CharField(max_length=50, blank=True)
    route = models.CharField(max_length=50, choices=ROUTE_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Prescription for {self.patient.patient_id} - {self.medicine_name}"

class TreatmentPlan(models.Model):
    PRIORITY_CHOICES = [('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Urgent', 'Urgent')]
    STATUS_CHOICES = [('active', 'Active'), ('completed', 'Completed'), ('on-hold', 'On Hold')]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='treatment_plans')
    doctor = models.ForeignKey(Staff, limit_choices_to={'role': 'doctor'}, on_delete=models.CASCADE)
    treatment_type = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    expected_end_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    outcomes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Treatment: {self.treatment_type} for {self.patient.patient_id}"
