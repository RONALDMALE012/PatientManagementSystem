from django.urls import path
from . import views
urlpatterns = [
    path('', views.visit_list, name='visit_list'),
    path('add/', views.add_visit, name='add_visit'),
    path('edit/<int:id>/', views.edit_visit, name='edit_visit'),
    path('delete/<int:id>/', views.delete_visit, name='delete_visit'),
]
