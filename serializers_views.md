# SERIALIZERS.PY AND VIEWS.PY FOR ALL APPS

## staff/serializers.py

```python
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
```

## staff/views.py

```python
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Staff
from .serializers import StaffSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def doctors(self, request):
        doctors = Staff.objects.filter(role='doctor')
        serializer = self.get_serializer(doctors, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def nurses(self, request):
        nurses = Staff.objects.filter(role='nurse')
        serializer = self.get_serializer(nurses, many=True)
        return Response(serializer.data)
```

## staff/urls.py

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffViewSet

router = DefaultRouter()
router.register(r'', StaffViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

## patients/serializers.py

```python
from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
```

## patients/views.py

```python
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_admitted', 'gender', 'blood_group']
    search_fields = ['patient_id', 'first_name', 'last_name', 'phone']
    ordering_fields = ['created_at', 'first_name']
```

## patients/urls.py

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet

router = DefaultRouter()
router.register(r'', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

## doctor/serializers.py

```python
from rest_framework import serializers
from .models import Prescription, TreatmentPlan

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class TreatmentPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentPlan
        fields = '__all__'
```

## doctor/views.py

```python
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Prescription, TreatmentPlan
from .serializers import PrescriptionSerializer, TreatmentPlanSerializer

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['patient', 'doctor', 'priority', 'route']
    search_fields = ['medicine_name', 'patient__patient_id']

class TreatmentPlanViewSet(viewsets.ModelViewSet):
    queryset = TreatmentPlan.objects.all()
    serializer_class = TreatmentPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['patient', 'doctor', 'status', 'priority']
    search_fields = ['treatment_type', 'patient__patient_id']
```

## doctor/urls.py

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrescriptionViewSet, TreatmentPlanViewSet

router = DefaultRouter()
router.register(r'prescriptions', PrescriptionViewSet, basename='prescription')
router.register(r'treatment-plans', TreatmentPlanViewSet, basename='treatment-plan')

urlpatterns = [
    path('', include(router.urls)),
]
```

## nurse/serializers.py

```python
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
```

## nurse/views.py

```python
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Admission, PatientObservation
from .serializers import AdmissionSerializer, PatientObservationSerializer

class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['patient', 'admission_type']
    search_fields = ['patient__patient_id', 'room_number']
    ordering_fields = ['admission_date_time']

class PatientObservationViewSet(viewsets.ModelViewSet):
    queryset = PatientObservation.objects.all()
    serializer_class = PatientObservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['patient', 'nurse']
```

## nurse/urls.py

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdmissionViewSet, PatientObservationViewSet

router = DefaultRouter()
router.register(r'admissions', AdmissionViewSet, basename='admission')
router.register(r'observations', PatientObservationViewSet, basename='observation')

urlpatterns = [
    path('', include(router.urls)),
]
```

## equipment/serializers.py

```python
from rest_framework import serializers
from .models import Equipment, MaintenanceLog

class MaintenanceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceLog
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    maintenance_logs = MaintenanceLogSerializer(many=True, read_only=True)
    
    class Meta:
        model = Equipment
        fields = '__all__'
```

## equipment/views.py

```python
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Equipment, MaintenanceLog
from .serializers import EquipmentSerializer, MaintenanceLogSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'equipment_type']
    search_fields = ['equipment_name', 'equipment_id']

class MaintenanceLogViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceLog.objects.all()
    serializer_class = MaintenanceLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['equipment']
```

## equipment/urls.py

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EquipmentViewSet, MaintenanceLogViewSet

router = DefaultRouter()
router.register(r'equipment', EquipmentViewSet, basename='equipment')
router.register(r'maintenance-logs', MaintenanceLogViewSet, basename='maintenance-log')

urlpatterns = [
    path('', include(router.urls)),
]
```

## reports/serializers.py

```python
from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
```

## reports/views.py

```python
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Report
from .serializers import ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['patient', 'report_type']
    search_fields = ['patient__patient_id']
    ordering_fields = ['report_date', 'created_at']
```

## reports/urls.py

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReportViewSet

router = DefaultRouter()
router.register(r'', ReportViewSet, basename='report')

urlpatterns = [
    path('', include(router.urls)),
]
```

