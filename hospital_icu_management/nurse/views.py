from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Admission, PatientObservation
from .forms import AdmissionForm, PatientObservationForm
from rest_framework import viewsets
from .models import Admission
from .serializers import AdmissionSerializer


@login_required
def admissions_list(request):
    admissions = Admission.objects.all()  # Update based on your model name
    return render(request, 'nurse/admission_list.html', {'admissions': admissions})


@login_required
def admission_detail(request, pk):
    admission = get_object_or_404(Admission, pk=pk)
    context = {'admission': admission}
    return render(request, 'nurse/admission_detail.html', context)


@login_required
def admission_create(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            admission = form.save(commit=False)
            admission.nurse = request.user.staff
            admission.save()
            messages.success(request, 'Admission recorded successfully!')
            return redirect('nurse:admission_detail', pk=admission.pk)
    else:
        form = AdmissionForm()
    
    context = {'form': form}
    return render(request, 'nurse/admission_form.html', context)


@login_required
def admission_update(request, pk):
    admission = get_object_or_404(Admission, pk=pk)
    if request.method == 'POST':
        form = AdmissionForm(request.POST, instance=admission)
        if form.is_valid():
            form.save()
            messages.success(request, 'Admission updated successfully!')
            return redirect('nurse:admission_detail', pk=admission.pk)
    else:
        form = AdmissionForm(instance=admission)
    
    context = {'form': form, 'object': admission}
    return render(request, 'nurse/admission_form.html', context)


@login_required
def treatment_history_list(request):
    history = PatientObservation.objects.select_related('patient', 'nurse').all().order_by('-observation_date_time')
    context = {'treatment_history': history}
    return render(request, 'nurse/treatment_history_list.html', context)


@login_required
def treatment_history_detail(request, pk):
    observation = get_object_or_404(PatientObservation, pk=pk)
    context = {'observation': observation}
    return render(request, 'nurse/treatment_history_detail.html', context)


@login_required
def treatment_history_create(request):
    if request.method == 'POST':
        form = PatientObservationForm(request.POST)
        if form.is_valid():
            observation = form.save(commit=False)
            observation.nurse = request.user.staff
            observation.save()
            messages.success(request, 'Treatment history recorded successfully!')
            return redirect('nurse:treatment_history_list')
    else:
        form = PatientObservationForm()
    
    context = {'form': form}
    return render(request, 'nurse/treatment_history_form.html', context)

@login_required
def admission_create(request):
    if request.method == "POST":
        form = AdmissionForm(request.POST)
        if form.is_valid():
            admission = form.save(commit=False)
            admission.nurse = request.user.staff
            admission.save()
            messages.success(request, 'Admission recorded successfully!')
            return redirect('nurse:admission_list')
    else:
        form = AdmissionForm()
    context = {'form': form}
    return render(request, 'nurse/admission_form.html', context)


class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer