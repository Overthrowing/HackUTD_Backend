from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
import base64

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

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class Doctors(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)


class DoctorView(APIView):
    def get(self, request, id):
        doctor = Doctor.objects.get(id=id)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class AddPatient(APIView):
    def post(self, request):
        pass


class RoomCheckIn(APIView):
    def post(self, request):
        raw_room_id = request.data['room_id']
        patient_id = request.data['patient_id']
        room = get_object_or_404(Room, id=base64.b64decode(raw_room_id)-100000)
        patient = get_object_or_404(Patient, id=patient_id)
        patient.room = room
        return Response(status=200)