from django.shortcuts import render
from django.shortcuts import render
from .serializer import StudentSerializer 
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from crudapi.throtlling import RateThrottle

# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    Authentication_class=[SessionAuthentication]
    permission_class=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle,RateThrottle]