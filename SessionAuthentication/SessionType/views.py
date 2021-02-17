from django.shortcuts import render
from . models import Student
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions
# Create your views here.

class StudentSessionAuthentication(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAdminUser]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    permission_classes=[DjangoModelPermissions]