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


class Rooms(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

class RoomCheckIn(APIView):
    def post(self, request):
        raw_room_id = request.data['room_id']
        patient_id = request.data['patient_id']
        room = get_object_or_404(Room, id=raw_room_id)
        patient = get_object_or_404(Patient, id=patient_id)
        patient.room = room
        patient.save()
        return Response(status=200)
    

class RegisterPatient(APIView):
    def post(self, request):
        raw_image_data = request.data['image']
        # OCR Image
        patient = Patient.objects.get_or_create(id=1)
        patient.first_name = "Tricera"
        patient.last_name = "Tops"
        patient.gender = "F"
        patient.age = 67000000
        patient.save()
        return Response(PatientSerializer(patient).data)
    

class RenderRoom(APIView):
    def get(self, request, room_id):
        room = get_object_or_404(Room, id=room_id+1)
        serializer = RoomSerializer(room)
        out = serializer.data
        match serializer.data['priority']:
            case "H":
                out['color'] = "#DB5461"
            case "M":
                out['color'] = "#EDEBA0"
            case "L":
                out['color'] = "#D1EFB5"


        # Wheelchairs
        wheelchairs = room.chairs.all()
        serializer = WheelChairSerializer(wheelchairs, many=True)
        out['wheelchairs'] = serializer.data

        # Patients
        patients = room.patients.all()
        serializer = PatientSerializer(patients, many=True)
        out['patients'] = serializer.data
        
        return Response(out)
    
class FindWheelChairs(APIView):
    def get(self, request, room_id):
        room = get_object_or_404(Room, id=room_id+1)
        wheelchairs = room.chairs.all()
        serializer = WheelChairSerializer(wheelchairs, many=True)
        return Response(serializer.data)