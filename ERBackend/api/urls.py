from django.urls import path

from . import views

app_name = 'api'

# URL patterns for the ER app
urlpatterns = [
    path('patients/', views.Patients.as_view(), name='patients'),
    path('patient/<int:id>/', views.PatientView.as_view(), name='patient'),
    path('patient/', views.PatientView.as_view(), name='patient'),
    path('doctor/<int:id>/', views.DoctorView.as_view(), name='doctor'),

    path('doctors/', views.Doctors.as_view(), name='doctors'),
]