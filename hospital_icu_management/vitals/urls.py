from django.urls import path
from . import views

urlpatterns = [
    path('realtime/', views.realtime_vitals_dashboard, name='realtime_vitals_dashboard'),
    path('api/vitals/', views.get_realtime_vitals, name='get_realtime_vitals'),
    path('api/vitals/<int:patient_id>/', views.get_realtime_vitals, name='get_patient_vitals'),
    path('api/generate/', views.generate_vital_reading, name='generate_vital_reading'),
    path('api/generate/<int:patient_id>/', views.generate_vital_reading, name='generate_patient_vital'),
]

