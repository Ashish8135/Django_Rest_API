from django.shortcuts import render
from . models import Student
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
# Create your views here.

class StudentAuthentication(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    permission_classes=[AllowAny]
    permission_classes=[IsAdminUser]


