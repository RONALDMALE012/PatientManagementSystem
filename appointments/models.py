from django.db import models
from patients.models import Patient
# Create your models here.

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )
    doctor = models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.patient} - {self.appointment_date}"
