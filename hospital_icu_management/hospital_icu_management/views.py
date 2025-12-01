# accounts/views.py or hospital_icu_management/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from staff.models import Staff

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        role = request.POST.get('role')
        
        # Validation
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'registration/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'registration/register.html')
        
        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name
        )
        
        # Create staff profile
        Staff.objects.create(
            user=user,
            role=role,
            phone='',  # Can be added later
            department='General'
        )
        
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')
    
    return render(request, 'registration/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.get_full_name()}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'registration/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')

@login_required
def settings_view(request):
    return render(request, 'registration/settings.html')

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    from patients.models import Patient
    from staff.models import Staff
    from nurse.models import Admission
    
    context = {
        'total_patients': Patient.objects.count(),
        'active_staff': Staff.objects.filter(availability_status=True).count(),
        'icu_occupied': Patient.objects.filter(status='admitted').count(),
        'critical_cases': Patient.objects.filter(status='critical').count(),
        'recent_admissions': Admission.objects.select_related('patient', 'nurse').order_by('-admission_date_time')[:5],
        'alerts': []  # Add your alert logic here
    }
    return render(request, 'home.html', context)
