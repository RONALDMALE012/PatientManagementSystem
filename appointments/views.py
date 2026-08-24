from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from .forms import AppointmentForm
def appointment_list(request):
    appointments = Appointment.objects.select_related('patient').all()
    return render(request, 'appointments/appointment_list.html', {
        'appointments': appointments
    })
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointment_form.html', {
        'form': form
    })
def edit_appointment(request, id):
    appointment = get_object_or_404(Appointment, pk=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/appointment_form.html', {
        'form': form
    })
def delete_appointment(request, id):
    appointment = get_object_or_404(Appointment, pk=id)
    appointment.delete()
    return redirect('appointment_list')
