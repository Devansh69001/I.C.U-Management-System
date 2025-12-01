from django.urls import path
from . import views

urlpatterns = [
    # Prescription URLs
    path('prescriptions/create/', views.prescription_create, name='prescription_create'),
    path('prescriptions/', views.prescription_list, name='prescription_list'),
    path('prescriptions/<int:pk>/', views.prescription_detail, name='prescription_detail'),
    path('prescriptions/create/', views.prescription_create, name='prescription_create'),
    path('prescriptions/<int:pk>/update/', views.prescription_update, name='prescription_update'),

    # Treatment Plan URLs
    path('treatment-plans/', views.treatment_plan_list, name='treatment_plan_list'),
    path('treatment-plans/<int:pk>/', views.treatment_plan_detail, name='treatment_plan_detail'),
    path('treatment-plans/create/', views.treatment_plan_create, name='treatment_plan_create'),
    path('treatment-plans/<int:pk>/update/', views.treatment_plan_update, name='treatment_plan_update'),
    path('treatment-plans/create/', views.treatment_plan_create, name='treatment_plan_create')

]
