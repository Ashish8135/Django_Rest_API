from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
# Create your views here.

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu=Student.objects.all()
        serializer=StudentSerializer
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id)
            serializer=StudentSerializer
            return Response(serializer.data)


