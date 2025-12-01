from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipment_list, name='equipment_list'),
    path('<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('create/', views.equipment_create, name='equipment_create'),
    path('<int:pk>/update/', views.equipment_update, name='equipment_update'),
]
