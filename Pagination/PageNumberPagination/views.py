  
from django.shortcuts import render
from PageNumberPagination.serializer import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from PageNumberPagination.pagination import MyPageNumberPagination
# from rest_framework.filters import SearchFilter
# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class=MyPageNumberPagination

# second method for pagination.
