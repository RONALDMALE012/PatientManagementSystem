from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from patients.models import Patient
from appointments.models import Appointment
from visits.models import Visit
@login_required
def dashboard(request):
    total_patients = Patient.objects.count()
    total_appointments = Appointment.objects.count()
    total_visits = Visit.objects.count()
    total_users = User.objects.count()

    recent_patients = Patient.objects.order_by('-created_at')[:5]
    recent_appointments = Appointment.objects.order_by('-appointment_date')[:5]
    context = {
        'total_patients': total_patients,
        'total_appointments': total_appointments,
        'total_visits': total_visits,
        'total_users': total_users,
        'recent_patients': recent_patients,
        'recent_appointments': recent_appointments,
    }
    return render(request, 'dashboard/index.html', context)

