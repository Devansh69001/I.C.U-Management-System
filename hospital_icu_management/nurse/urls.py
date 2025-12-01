from django.urls import path
from . import views
app_name = 'nurse'

urlpatterns = [
    # Admissions URLs
    path('admissions/', views.admissions_list, name='admissions_list'),
    path('admissions/<int:pk>/', views.admission_detail, name='admission_detail'),
    path('admissions/create/', views.admission_create, name='admission_create'),
    path('admissions/<int:pk>/update/', views.admission_update, name='admission_update'),

    # Treatment History URLs
    path('treatment-history/', views.treatment_history_list, name='treatment_history_list'),
    path('treatment-history/<int:pk>/', views.treatment_history_detail, name='treatment_history_detail'),
    path('treatment-history/create/', views.treatment_history_create, name='treatment_history_create'),
]
