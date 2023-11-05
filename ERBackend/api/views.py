from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from models import *

# Create your views here.
class PatientView(APIView):
    def get(self, request):
        response = Response()
        response.data = Patient.objects.all().values()
        return response
    def post(self, request):
        response = Response()
        response.data = Patient.objects.create(**request.data)
        return response
        