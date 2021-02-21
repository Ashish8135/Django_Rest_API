from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
