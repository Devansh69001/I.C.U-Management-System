from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from accounts.views import CustomLoginView, profile_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    
    # Home and Dashboard
    path('', views.home_view, name='home'),
    
    # Authentication
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('settings/', views.settings_view, name='settings'),
    path('profile/', profile_view, name='profile'),
    
    # App URLs
    path('patients/', include('patients.urls')),
    path('staff/', include('staff.urls')),
    path('doctor/', include('doctor.urls')),
    path('nurse/', include('nurse.urls', namespace='nurse')),
    path('equipment/', include('equipment.urls')),
    path('reports/', include('reports.urls')),
    path('vitals/', include('vitals.urls')),
    
    # API URLs
    path('api/', include('api.urls')),
    path('alerts/', include('alerts.urls')),

    path('reports/', include('reports.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
