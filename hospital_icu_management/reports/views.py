from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from patients.models import Patient, VitalReading
from staff.models import Staff
from doctor.models import Prescription
from nurse.models import Admission
from django.db.models import Q
import json
from datetime import timedelta
from django.utils import timezone

'''@login_required
def report_list(request):
    context = {
        'total_patients': Patient.objects.count(),
        'admitted_patients': Patient.objects.filter(status='admitted').count(),
        'critical_patients': Patient.objects.filter(status='critical').count(),
        'total_staff': Staff.objects.count(),
        'total_prescriptions': Prescription.objects.count(),
        'total_admissions': Admission.objects.count(),
    }
    return render(request, 'reports/report_list.html', context)'''
@login_required
def report_list(request):
    # Get all admitted patients
    admitted_patients = Patient.objects.filter(
        Q(status__iexact='admitted') | Q(status__iexact='critical')
    ).order_by('-id')
    
    context = {
        'patients': admitted_patients,
    }
    return render(request, 'reports/report_list.html', context)

@login_required
def patient_vitals_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    
    # Get vitals from last 7 days
    seven_days_ago = timezone.now() - timedelta(days=7)
    vitals = VitalReading.objects.filter(
        patient=patient,
        timestamp__gte=seven_days_ago
    ).order_by('timestamp')
    
    # Prepare data for charts
    timestamps = [v.timestamp.strftime('%Y-%m-%d %H:%M') for v in vitals]
    bp_systolic = [v.blood_pressure_systolic for v in vitals]
    bp_diastolic = [v.blood_pressure_diastolic for v in vitals]
    oxygen = [v.oxygen_saturation for v in vitals]
    heart_rate = [v.heart_rate for v in vitals]
    temperature = [float(v.temperature) if v.temperature else None for v in vitals]
    
    context = {
        'patient': patient,
        'vitals_count': vitals.count(),
        'timestamps': json.dumps(timestamps),
        'bp_systolic': json.dumps(bp_systolic),
        'bp_diastolic': json.dumps(bp_diastolic),
        'oxygen': json.dumps(oxygen),
        'heart_rate': json.dumps(heart_rate),
        'temperature': json.dumps(temperature),
    }
    return render(request, 'reports/patient_vitals_detail.html', context)
