from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from patients.models import Patient, VitalReading
from django.utils import timezone
from datetime import timedelta
import json
import random
from decimal import Decimal


@login_required
def realtime_vitals_dashboard(request):
    """Real-time vitals dashboard showing all patients with live graphs"""
    # Get all admitted patients (show all, even without vitals)
    patients = Patient.objects.filter(
        is_admitted=True
    ).order_by('-id')
    
    # If no admitted patients, show all patients for testing
    if not patients.exists():
        patients = Patient.objects.all()[:10]  # Show first 10 patients for testing
    
    context = {
        'patients': patients,
    }
    return render(request, 'vitals/realtime_dashboard.html', context)


def _calculate_vital_status(vital_type, value):
    """Calculate medical status of a vital sign"""
    if value is None:
        return 'normal'
    
    ranges = {
        'bp_systolic': {'normal': (90, 140), 'warning': (80, 90, 140, 160), 'critical': (0, 80, 160, 300)},
        'bp_diastolic': {'normal': (60, 90), 'warning': (50, 60, 90, 100), 'critical': (0, 50, 100, 300)},
        'spo2': {'normal': (95, 100), 'warning': (90, 95), 'critical': (0, 90)},
        'hr': {'normal': (60, 100), 'warning': (50, 60, 100, 120), 'critical': (0, 50, 120, 300)},
        'temp': {'normal': (36.1, 37.2), 'warning': (35.0, 36.1, 37.2, 38.0), 'critical': (0, 35.0, 38.0, 50)}
    }
    
    if vital_type not in ranges:
        return 'normal'
    
    r = ranges[vital_type]
    
    if vital_type in ['bp_systolic', 'bp_diastolic', 'hr']:
        if value < r['critical'][1] or value > r['critical'][2]:
            return 'critical'
        if value < r['warning'][0] or value > r['warning'][2]:
            return 'warning'
        if r['normal'][0] <= value <= r['normal'][1]:
            return 'normal'
    elif vital_type == 'spo2':
        if value < r['critical'][1]:
            return 'critical'
        if value < r['warning'][1]:
            return 'warning'
        if value >= r['normal'][0]:
            return 'normal'
    elif vital_type == 'temp':
        if value < r['critical'][1] or value > r['critical'][2]:
            return 'critical'
        if value < r['warning'][0] or value > r['warning'][2]:
            return 'warning'
        if r['normal'][0] <= value <= r['normal'][1]:
            return 'normal'
    
    return 'normal'


@login_required
def get_realtime_vitals(request, patient_id=None):
    """API endpoint to fetch real-time vitals data for a patient or all patients"""
    # Get vitals from last 1 hour for real-time monitoring
    one_hour_ago = timezone.now() - timedelta(hours=1)
    
    if patient_id:
        # Get vitals for specific patient
        try:
            patient = Patient.objects.get(id=patient_id)
            vitals = VitalReading.objects.filter(
                patient=patient,
                timestamp__gte=one_hour_ago
            ).order_by('timestamp')
            
            latest = vitals[0] if vitals.exists() else None
            latest_data = {
                'blood_pressure_systolic': latest.blood_pressure_systolic if latest and latest.blood_pressure_systolic else None,
                'blood_pressure_diastolic': latest.blood_pressure_diastolic if latest and latest.blood_pressure_diastolic else None,
                'oxygen_saturation': latest.oxygen_saturation if latest and latest.oxygen_saturation else None,
                'heart_rate': latest.heart_rate if latest and latest.heart_rate else None,
                'temperature': float(latest.temperature) if latest and latest.temperature else None,
                'timestamp': latest.timestamp.strftime('%Y-%m-%d %H:%M:%S') if latest else None,
            }
            
            # Calculate status for each vital
            if latest_data['blood_pressure_systolic']:
                latest_data['bp_status'] = _calculate_vital_status('bp_systolic', latest_data['blood_pressure_systolic'])
            if latest_data['oxygen_saturation']:
                latest_data['spo2_status'] = _calculate_vital_status('spo2', latest_data['oxygen_saturation'])
            if latest_data['heart_rate']:
                latest_data['hr_status'] = _calculate_vital_status('hr', latest_data['heart_rate'])
            if latest_data['temperature']:
                latest_data['temp_status'] = _calculate_vital_status('temp', latest_data['temperature'])
            
            data = {
                'patient_id': patient.id,
                'patient_name': f"{patient.first_name} {patient.last_name}",
                'status': patient.status or 'monitoring',
                'room_number': patient.room_number or '',
                'patient_id_display': patient.patient_id or str(patient.id),
                'timestamps': [v.timestamp.strftime('%H:%M:%S') for v in vitals],
                'blood_pressure_systolic': [v.blood_pressure_systolic for v in vitals],
                'blood_pressure_diastolic': [v.blood_pressure_diastolic for v in vitals],
                'oxygen_saturation': [v.oxygen_saturation for v in vitals],
                'heart_rate': [v.heart_rate for v in vitals],
                'temperature': [float(v.temperature) if v.temperature else None for v in vitals],
                'latest': latest_data
            }
            return JsonResponse(data)
        except Patient.DoesNotExist:
            return JsonResponse({'error': 'Patient not found'}, status=404)
    else:
        # Get vitals for all admitted patients (include all patients, even without vitals)
        patients = Patient.objects.filter(is_admitted=True)
        all_patients_data = []
        
        for patient in patients:
            vitals = VitalReading.objects.filter(
                patient=patient,
                timestamp__gte=one_hour_ago
            ).order_by('timestamp')
            
            latest_vital = vitals.first() if vitals.exists() else None
            
            # Include patient even if no vitals exist yet
            latest_data = {
                'blood_pressure_systolic': latest_vital.blood_pressure_systolic if latest_vital else None,
                'blood_pressure_diastolic': latest_vital.blood_pressure_diastolic if latest_vital else None,
                'oxygen_saturation': latest_vital.oxygen_saturation if latest_vital else None,
                'heart_rate': latest_vital.heart_rate if latest_vital else None,
                'temperature': float(latest_vital.temperature) if latest_vital and latest_vital.temperature else None,
                'timestamp': latest_vital.timestamp.strftime('%Y-%m-%d %H:%M:%S') if latest_vital else None,
            }
            
            # Calculate status for each vital
            if latest_data['blood_pressure_systolic']:
                latest_data['bp_status'] = _calculate_vital_status('bp_systolic', latest_data['blood_pressure_systolic'])
            if latest_data['oxygen_saturation']:
                latest_data['spo2_status'] = _calculate_vital_status('spo2', latest_data['oxygen_saturation'])
            if latest_data['heart_rate']:
                latest_data['hr_status'] = _calculate_vital_status('hr', latest_data['heart_rate'])
            if latest_data['temperature']:
                latest_data['temp_status'] = _calculate_vital_status('temp', latest_data['temperature'])
            
            patient_data = {
                'patient_id': patient.id,
                'patient_name': f"{patient.first_name} {patient.last_name}",
                'status': patient.status or 'monitoring',
                'room_number': patient.room_number or '',
                'patient_id_display': patient.patient_id or str(patient.id),
                'latest': latest_data,
                'timestamps': [v.timestamp.strftime('%H:%M:%S') for v in vitals[:20]],  # Last 20 readings
                'blood_pressure_systolic': [v.blood_pressure_systolic for v in vitals[:20]],
                'blood_pressure_diastolic': [v.blood_pressure_diastolic for v in vitals[:20]],
                'oxygen_saturation': [v.oxygen_saturation for v in vitals[:20]],
                'heart_rate': [v.heart_rate for v in vitals[:20]],
                'temperature': [float(v.temperature) if v.temperature else None for v in vitals[:20]],
            }
            all_patients_data.append(patient_data)
        
        return JsonResponse({'patients': all_patients_data}, safe=False)


@login_required
def generate_vital_reading(request, patient_id=None):
    """API endpoint to generate a new vital reading for a patient (simulation)"""
    if not patient_id:
        # Generate for all admitted patients, or all patients if none admitted
        patients = Patient.objects.filter(is_admitted=True)
        if not patients.exists():
            # If no admitted patients, use all patients for testing
            patients = Patient.objects.all()[:10]
        generated_readings = []
        
        for patient in patients:
            # Get last vital reading to base new reading on (for realistic variation)
            last_vital = VitalReading.objects.filter(patient=patient).order_by('-timestamp').first()
            
            # Generate new vital reading with realistic variations
            new_vital = _generate_realistic_vital(patient, last_vital)
            generated_readings.append({
                'patient_id': patient.id,
                'patient_name': f"{patient.first_name} {patient.last_name}",
                'vital': {
                    'blood_pressure_systolic': new_vital.blood_pressure_systolic,
                    'blood_pressure_diastolic': new_vital.blood_pressure_diastolic,
                    'oxygen_saturation': new_vital.oxygen_saturation,
                    'heart_rate': new_vital.heart_rate,
                    'temperature': float(new_vital.temperature) if new_vital.temperature else None,
                    'timestamp': new_vital.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                }
            })
        
        return JsonResponse({'readings': generated_readings}, safe=False)
    else:
        # Generate for specific patient
        try:
            patient = Patient.objects.get(id=patient_id)
            last_vital = VitalReading.objects.filter(patient=patient).order_by('-timestamp').first()
            
            new_vital = _generate_realistic_vital(patient, last_vital)
            
            return JsonResponse({
                'patient_id': patient.id,
                'patient_name': f"{patient.first_name} {patient.last_name}",
                'vital': {
                    'blood_pressure_systolic': new_vital.blood_pressure_systolic,
                    'blood_pressure_diastolic': new_vital.blood_pressure_diastolic,
                    'oxygen_saturation': new_vital.oxygen_saturation,
                    'heart_rate': new_vital.heart_rate,
                    'temperature': float(new_vital.temperature) if new_vital.temperature else None,
                    'timestamp': new_vital.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                }
            })
        except Patient.DoesNotExist:
            return JsonResponse({'error': 'Patient not found'}, status=404)


def _generate_realistic_vital(patient, last_vital=None):
    """Generate a realistic vital reading based on patient status and last reading"""
    
    # Base values (normal ranges)
    if last_vital:
        # Base new reading on last reading with small variations
        base_systolic = last_vital.blood_pressure_systolic or 120
        base_diastolic = last_vital.blood_pressure_diastolic or 80
        base_spo2 = last_vital.oxygen_saturation or 98
        base_hr = last_vital.heart_rate or 72
        base_temp = float(last_vital.temperature) if last_vital.temperature else 37.0
    else:
        # Initial values based on patient status
        if patient.status and patient.status.lower() == 'critical':
            base_systolic = random.randint(80, 100)
            base_diastolic = random.randint(50, 70)
            base_spo2 = random.randint(85, 92)
            base_hr = random.randint(100, 130)
            base_temp = random.uniform(38.0, 39.5)
        else:
            base_systolic = random.randint(110, 130)
            base_diastolic = random.randint(70, 85)
            base_spo2 = random.randint(95, 100)
            base_hr = random.randint(60, 90)
            base_temp = random.uniform(36.5, 37.5)
    
    # Add realistic variation (±5% for most, ±10% for critical patients)
    variation = 0.10 if patient.status and patient.status.lower() == 'critical' else 0.05
    
    # Generate new values with small random variations
    new_systolic = max(60, min(180, int(base_systolic + random.uniform(-base_systolic * variation, base_systolic * variation))))
    new_diastolic = max(40, min(120, int(base_diastolic + random.uniform(-base_diastolic * variation, base_diastolic * variation))))
    new_spo2 = max(70, min(100, int(base_spo2 + random.uniform(-base_spo2 * variation, base_spo2 * variation))))
    new_hr = max(40, min(180, int(base_hr + random.uniform(-base_hr * variation, base_hr * variation))))
    new_temp = max(35.0, min(42.0, base_temp + random.uniform(-base_temp * variation, base_temp * variation)))
    
    # Create new vital reading
    new_vital = VitalReading.objects.create(
        patient=patient,
        blood_pressure_systolic=new_systolic,
        blood_pressure_diastolic=new_diastolic,
        oxygen_saturation=new_spo2,
        heart_rate=new_hr,
        temperature=Decimal(str(round(new_temp, 1)))
    )
    
    return new_vital
