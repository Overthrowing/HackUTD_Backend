from django.urls import path

from . import views

app_name = 'api'

# URL patterns for the CyRanch Connect app
urlpatterns = [
    path('patients/', views.Patients.as_view(), name='patients'),
]