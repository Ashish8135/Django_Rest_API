from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework import status
# Create your views here.

class RegionListApiView(viewsets.ModelViewSet):
    queryset=Region.objects.all()
    serializer_class=RegionSerializer

class CountryListApiView(viewsets.ModelViewSet):
    queryset=Country.objects.all()
    serializer_class=CountrySerializer

class StateListApiView(viewsets.ModelViewSet):
    queryset=State.objects.all()
    serializer_class=StateSerializer

class CityListApiView(viewsets.ModelViewSet):
    queryset=City.objects.all()
    serializer_class=CitySerializer

class LocationListApiView(viewsets.ModelViewSet):
    queryset=LocationData.objects.all()
    serializer_class=LocationSerializer



