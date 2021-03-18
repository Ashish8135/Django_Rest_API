from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from .pagination import MyCursorPagination
# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class=MyLimitPagination
    pagination_class=MyCursorPagination
