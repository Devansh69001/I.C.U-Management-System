from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patients.views import PatientViewSet
from staff.views import StaffViewSet
from doctor.views import PrescriptionViewSet
from nurse.views import AdmissionViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'prescriptions', PrescriptionViewSet, basename='prescription')
router.register(r'admissions', AdmissionViewSet, basename='admission')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),  # optional browsable API auth
]
