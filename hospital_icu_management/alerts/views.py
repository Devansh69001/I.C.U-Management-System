# alerts/views.py
from django.shortcuts import render
from patients.models import Patient


def alerts_list(request):
    # Only fetch patients with "Critical" status (case-insensitive)
    critical_patients = Patient.objects.filter(status__iexact='Critical')
    return render(request, 'alerts/alerts_list.html', {'alerts': critical_patients})
