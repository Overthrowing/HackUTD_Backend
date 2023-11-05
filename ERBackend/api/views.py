from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class Patients(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)


class PatientView(APIView):
    def get(self, request, id):
        patient = Patient.objects.get(id=id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)