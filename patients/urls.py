from django.urls import path
from . import views
urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('add/', views.add_patient, name='add_patient'),
    path('edit/<int:id>/', views.edit_patient, name='edit_patient'),
    path('delete/<int:id>/', views.delete_patient, name='delete_patient'),
    path('profile/<int:id>/', views.patient_profile, name='patient_profile'),
    path('patients/pdf/', views.export_patient_pdf, name='patient_pdf'),
    path('patients/excel/', views.export_patient_excel, name='patient_excel'),

]
