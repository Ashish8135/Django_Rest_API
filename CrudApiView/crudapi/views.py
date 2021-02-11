from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer

# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])


