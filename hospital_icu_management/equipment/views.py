from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Equipment
from .forms import EquipmentForm

@login_required
def equipment_list(request):
    equipment_list = Equipment.objects.all().order_by('equipment_name')
    context = {'equipment_list': equipment_list}
    return render(request, 'equipment/equipment_list.html', context)

@login_required
def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    context = {'equipment': equipment}
    return render(request, 'equipment/equipment_detail.html', context)

@login_required
def equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.save()
            messages.success(request, 'Equipment added successfully!')
            return redirect('equipment_detail', pk=equipment.pk)
    else:
        form = EquipmentForm()
    
    context = {'form': form}
    return render(request, 'equipment/equipment_form.html', context)

@login_required
def equipment_update(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipment updated successfully!')
            return redirect('equipment_detail', pk=equipment.pk)
    else:
        form = EquipmentForm(instance=equipment)
    
    context = {'form': form, 'object': equipment}
    return render(request, 'equipment/equipment_form.html', context)
