from rest_framework import serializers
from .models import Admission, PatientObservation

class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = '__all__'

class PatientObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientObservation
        fields = '__all__'