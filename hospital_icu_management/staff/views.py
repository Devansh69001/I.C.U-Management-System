from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Staff
from .forms import StaffForm  # Assuming you have StaffForm defined for create/update
from rest_framework import viewsets
from .models import Staff
from .serializers import StaffSerializer


@login_required
def staff_list(request):
    staff_members = Staff.objects.all()
    doctor_count = Staff.objects.filter(role='doctor').count()
    nurse_count = Staff.objects.filter(role='nurse').count()
    admin_count = Staff.objects.filter(role='admin').count()
    context = {
        'staff_members': staff_members,
        'doctor_count': doctor_count,
        'nurse_count': nurse_count,
        'admin_count': admin_count,
    }
    return render(request, 'staff/staff_list.html', context)


@login_required
def staff_detail(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    context = {'staff': staff}
    return render(request, 'staff/staff_detail.html', context)


@login_required
def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            # Additional check:
            employee_id = form.cleaned_data.get('employee_id')
            if not employee_id:
                messages.error(request, "Employee ID is required.")
                return render(request, 'staff/staff_form.html', {'form': form})
            if Staff.objects.filter(employee_id=employee_id).exists():
                messages.error(request, "Employee ID already exists.")
                return render(request, 'staff/staff_form.html', {'form': form})
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff/staff_form.html', {'form': form})



@login_required
def staff_update(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff member updated successfully!')
            return redirect('staff_detail', pk=staff.pk)
    else:
        form = StaffForm(instance=staff)
    context = {'form': form, 'object': staff}
    return render(request, 'staff/staff_form.html', context)

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer