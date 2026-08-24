from django.db import models
from patients.models import Patient

# Create your models here.
class Visit(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )
    doctor = models.CharField(max_length=100)
    diagnosis = models.TextField()
    treatment = models.TextField()
    prescription = models.TextField()
    notes = models.TextField(blank=True)
    visit_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.patient} - {self.visit_date}"