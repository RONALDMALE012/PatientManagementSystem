from django.http import request
from django.shortcuts import render, redirect, get_object_or_404

from appointments.models import Appointment
from visits.models import Visit
from .models import Patient
from .forms import PatientForm
from django.db.models import Q
from django.contrib import messages
from django.utils.dateparse import parse_date
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import openpyxl
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required

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
            messages.success(request, "Patient registered successfully.")
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
            messages.success(request, "Patient updated successfully.")
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/patient_form.html', {
        'form': form
    })
def delete_patient(request, id):
    patient = get_object_or_404(Patient, pk=id)
    patient.delete()
    messages.success(request, "Patient deleted successfully.")
    return redirect('patient_list')

def patient_list(request):
    query = request.GET.get('q')
    if query:
        patients = Patient.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone__icontains=query)
        )
    else:
        patients = Patient.objects.all()
    return render(request,
        'patients/patient_list.html',
        {'patients': patients})
def patient_profile(request, id):
    patient = get_object_or_404(Patient, pk=id)
    visits = Visit.objects.filter(patient=patient)
    appointments = Appointment.objects.filter(patient=patient)
    return render(
        request,
        'patients/profile.html',
        {
            'patient': patient,
            'visits': visits,
            'appointments': appointments
        }
    )
def patient_report(request):
    start = request.GET.get("start_date")
    end = request.GET.get("end_date")
    patients = Patient.objects.all()
    if start and end:
        patients = patients.filter(
            created_at__date__range=[parse_date(start), parse_date(end)]
        )
    return render(request, "reports/patient_report.html", {
        "patients": patients
    })
def export_patient_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="patients.pdf"'
    p = canvas.Canvas(response)
    y = 800
    for patient in Patient.objects.all():
        p.drawString(
            50,
            y,
            f"{patient.first_name} {patient.last_name}"
        )
        y -= 20
    p.save()
    return response
def export_patient_excel(request):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append([
        "ID",
        "Name",
        "Gender",
        "Phone"
    ])
    for patient in Patient.objects.all():
        sheet.append([
            patient.patient_id,
            patient.first_name + " " + patient.last_name,
            patient.gender,
            patient.phone,
        ])
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="patients.xlsx"'
    workbook.save(response)
    return response






