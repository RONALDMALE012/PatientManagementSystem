from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {
        'patients': patients
    })
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patients/patient_form.html', {
        'form': form
    })
def edit_patient(request, id):
    patient = get_object_or_404(Patient, pk=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/patient_form.html', {
        'form': form
    })
def delete_patient(request, id):
    patient = get_object_or_404(Patient, pk=id)
    patient.delete()
    return redirect('patient_list')

