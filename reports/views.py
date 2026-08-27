from django.shortcuts import render
from patients.models import Patient
from appointments.models import Appointment
from visits.models import Visit
def reports_home(request):
    return render(request, 'reports/index.html')
def patient_report(request):
    patients = Patient.objects.all()
    return render(request, 'reports/patient_report.html', {
        'patients': patients
    })
def appointment_report(request):
    appointments = Appointment.objects.all()
    return render(request, 'reports/appointment_report.html', {
        'appointments': appointments
    })
def visit_report(request):
    visits = Visit.objects.all()
    return render(request, 'reports/visit_report.html', {
        'visits': visits
    })

