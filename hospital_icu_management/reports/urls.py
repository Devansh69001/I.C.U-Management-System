from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('patient/<int:patient_id>/vitals/', views.patient_vitals_detail, name='patient_vitals_detail'),
]
