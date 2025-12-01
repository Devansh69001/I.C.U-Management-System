from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_list, name='staff_list'),
    path('<int:pk>/', views.staff_detail, name='staff_detail'),
    path('create/', views.staff_create, name='staff_create'),
    path('<int:pk>/update/', views.staff_update, name='staff_update'),
]
