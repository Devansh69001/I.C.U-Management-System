from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Staff

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Staff
        fields = ['id', 'user', 'role', 'employee_id', 'specialization', 'phone', 'availability_status', 'shift', 'department', 'years_of_experience', 'date_joined']