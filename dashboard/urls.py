# dashboard/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='home'),
    path('maintenance/', views.maintenance_view, name='maintenance'),
    path('maintenance_success/', views.maintenance_success_view, name='maintenance_success'),
    path('submit_maintenance/', views.submit_maintenance_form, name='submit_maintenance_form'),
    path('database/', views.database_contents_view, name='database_contents'),   # Corrected view function here
    # Other URL patterns...
]
