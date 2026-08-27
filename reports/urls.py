from django.urls import path
from . import views
urlpatterns = [
    path('', views.reports_home, name='reports'),
    path('patients/', views.patient_report, name='patient_report'),
    path('appointments/', views.appointment_report, name='appointment_report'),
    path('visits/', views.visit_report, name='visit_report'),
]