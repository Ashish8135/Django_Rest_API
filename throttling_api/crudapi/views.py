from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView,RetrieveDestroyAPIView
from rest_framework.throttling import ScopedRateThrottle
# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'

class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='createstu'

class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='updatestu'

class StudentRetrieve(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='retrievestu'

class Studentdelete(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='deletestu'

# Same approach done in a single class
class StudentGetPost(ListAPIView,CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentPutDel(UpdateAPIView,RetrieveAPIView,DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


# Combination class of Crud

class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer