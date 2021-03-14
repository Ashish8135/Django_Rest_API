from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    # filtering the data by the admin 
    # queryset = Student.objects.filter(passby='ashish')
    serializer_class = StudentSerializer
    def get_queryset(self):
        user=self.request.user
        return Student.objects.filter(passby=user)
