from django.shortcuts import render
from .models import Student
from rest_framework.response import Response
from .serializer import StudentSerializer
from rest_framework.views import APIView
# Create your views here.

class StudentApi(APIView):
    def get(self,request,pk=None,format=None):
        id=pk 
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)

    
    def get(self,request,pk=None,format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data inserted successfully'})
        return Response(serializer.errors)

    def get(self,request,pk=None,format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated successfully'})
        return Response(serializer.errors)

    def get(self,request,pk=None,format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data deleted successfully'})


