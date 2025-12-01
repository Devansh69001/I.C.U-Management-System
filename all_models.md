# MODELS.PY FILES FOR ALL APPS

## staff/models.py

```python
from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('admin', 'Administrator'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    employee_id = models.CharField(max_length=50, unique=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    availability_status = models.BooleanField(default=True)
    shift = models.CharField(max_length=50, choices=[('morning', 'Morning'), ('evening', 'Evening'), ('night', 'Night')])
    department = models.CharField(max_length=100, blank=True)
    years_of_experience = models.IntegerField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.role}"


## patients/models.py

```python
from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    BLOOD_GROUP_CHOICES = [('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')]
    
    patient_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    emergency_contact = models.CharField(max_length=20)
    emergency_contact_name = models.CharField(max_length=100)
    allergies = models.TextField(blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)
    is_admitted = models.BooleanField(default=False)
    admission_date = models.DateTimeField(blank=True, null=True)
    discharge_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.patient_id})"


## doctor/models.py

```python
from django.db import models
from patients.models import Patient
from staff.models import Staff

class Prescription(models.Model):
    PRIORITY_CHOICES = [('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Urgent', 'Urgent')]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Staff, limit_choices_to={'role': 'doctor'}, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=50)
    duration = models.CharField(max_length=50, blank=True)
    route = models.CharField(max_length=50, choices=[('oral', 'Oral'), ('intravenous', 'Intravenous'), ('intramuscular', 'Intramuscular'), ('topical', 'Topical')])
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


## nurse/models.py

```python
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


## equipment/models.py

```python
from django.db import models

class Equipment(models.Model):
    STATUS_CHOICES = [('available', 'Available'), ('in-use', 'In Use'), ('maintenance', 'Maintenance'), ('broken', 'Broken')]
    
    equipment_id = models.CharField(max_length=50, unique=True)
    equipment_name = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    purchase_date = models.DateField()
    warranty_expiry = models.DateField(blank=True, null=True)
    last_maintenance_date = models.DateField(blank=True, null=True)
    next_maintenance_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['equipment_name']

    def __str__(self):
        return f"{self.equipment_name} ({self.equipment_id})"


class MaintenanceLog(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='maintenance_logs')
    maintenance_date = models.DateTimeField(auto_now_add=True)
    maintenance_type = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    performed_by = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-maintenance_date']

    def __str__(self):
        return f"Maintenance: {self.equipment.equipment_name} - {self.maintenance_date.date()}"


## reports/models.py

```python
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
```

