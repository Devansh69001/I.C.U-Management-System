# accounts/views.py or hospital_icu_management/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from staff.models import Staff
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm 
from django.db import transaction, IntegrityError

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        role = request.POST.get('role', '').strip()
        phone = request.POST.get('phone', '').strip()
        employee_id = request.POST.get('employee_id', '').strip()

        # Validation
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'registration/register.html', request.POST)
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'registration/register.html', request.POST)
        if not employee_id:
            messages.error(request, "Employee ID is required.")
            return render(request, 'registration/register.html', request.POST)
        if Staff.objects.filter(employee_id=employee_id).exists():
            messages.error(request, "Employee ID already exists.")
            return render(request, 'registration/register.html', request.POST)

        try:
            with transaction.atomic():
                # Create User
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                    first_name=first_name,
                    last_name=last_name
                )

                # Create Staff profile
                Staff.objects.create(
                    user=user,
                    role=role,
                    employee_id=employee_id,
                    phone=phone,
                    department='General'
                )
                messages.success(request, 'Account created successfully! Please login.')
                return redirect('login')
        except IntegrityError:
            messages.error(request, "Sorry, there was a registration error (possible duplicate entry).")
            return render(request, 'registration/register.html', request.POST)
    else:
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

@login_required
def settings_view(request):
    # Pass user data, settings form, etc., as needed
    return render(request, "registration/settings.html", {})

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    from patients.models import Patient
    from staff.models import Staff
    from nurse.models import Admission
    
    context = {
        'total_patients': Patient.objects.count(),
        'active_staff': Staff.objects.filter(is_active=True).count(),
        'icu_occupied': Patient.objects.filter(status='admitted').count(),
        'critical_cases': Patient.objects.filter(status='critical').count(),
        'recent_admissions': Admission.objects.select_related('patient', 'nurse').order_by('-admission_date_time')[:5],
        'alerts': []  # Add your alert logic here
    }
    return render(request, 'home.html', context)

@login_required
def profile_view(request):
    return render(request, "registration/profile.html", {})

class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'registration/login.html'
