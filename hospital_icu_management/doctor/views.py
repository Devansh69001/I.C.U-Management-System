from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Prescription, TreatmentPlan
from .forms import PrescriptionForm, TreatmentPlanForm
from rest_framework import viewsets
from .models import Prescription
from .serializers import PrescriptionSerializer


@login_required
def prescription_list(request):
    prescriptions = Prescription.objects.select_related('patient', 'doctor').all().order_by('-created_at')
    context = {'prescriptions': prescriptions}
    return render(request, 'doctor/prescription_list.html', context)


@login_required
def prescription_detail(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    context = {'prescription': prescription}
    return render(request, 'doctor/prescription_detail.html', context)


@login_required
def prescription_create(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = request.user.staff
            prescription.save()
            messages.success(request, 'Prescription added successfully!')
            return redirect('prescription_detail', pk=prescription.pk)
    else:
        form = PrescriptionForm()
    
    context = {'form': form}
    return render(request, 'doctor/prescription_form.html', context)


@login_required
def prescription_update(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            messages.success(request, 'Prescription updated successfully!')
            return redirect('prescription_detail', pk=prescription.pk)
    else:
        form = PrescriptionForm(instance=prescription)
    
    context = {'form': form, 'object': prescription}
    return render(request, 'doctor/prescription_form.html', context)


@login_required
def treatment_plan_list(request):
    plans = TreatmentPlan.objects.select_related('patient', 'doctor').all().order_by('-created_at')
    context = {'treatment_plans': plans}
    return render(request, 'doctor/treatment_plan_list.html', context)


@login_required
def treatment_plan_detail(request, pk):
    plan = get_object_or_404(TreatmentPlan, pk=pk)
    context = {'treatment_plan': plan}
    return render(request, 'doctor/treatment_plan_detail.html', context)


@login_required
def treatment_plan_create(request):
    if request.method == 'POST':
        form = TreatmentPlanForm(request.POST)
        if form.is_valid():
            treatment_plan = form.save(commit=False)
            treatment_plan.doctor = request.user.staff
            treatment_plan.save()
            messages.success(request, 'Treatment plan created successfully!')
            return redirect('treatment_plan_detail', pk=treatment_plan.pk)
    else:
        form = TreatmentPlanForm()
    
    context = {'form': form}
    return render(request, 'doctor/treatment_plan_form.html', context)


@login_required
def treatment_plan_update(request, pk):
    plan = get_object_or_404(TreatmentPlan, pk=pk)
    if request.method == 'POST':
        form = TreatmentPlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Treatment plan updated successfully!')
            return redirect('treatment_plan_detail', pk=plan.pk)
    else:
        form = TreatmentPlanForm(instance=plan)
    
    context = {'form': form, 'object': plan}
    return render(request, 'doctor/treatment_plan_form.html', context)

@login_required
def prescription_create(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = request.user.staff  # Links doctor
            prescription.save()
            messages.success(request, 'Prescription added successfully!')
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()
    context = {'form': form}
    return render(request, 'doctor/prescription_form.html', context)

@login_required
def treatment_plan_create(request):
    if request.method == 'POST':
        form = TreatmentPlanForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.doctor = request.user.staff
            plan.save()
            messages.success(request, 'Treatment plan added successfully!')
            return redirect('treatment_plan_list')
    else:
        form = TreatmentPlanForm()
    context = {'form': form}
    return render(request, 'doctor/treatment_plan_form.html', context)


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer