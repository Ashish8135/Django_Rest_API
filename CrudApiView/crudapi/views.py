from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer

# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def studentapi(request):
    if request.method=='GET':
        id=request.data.get('id')
        if id is not None:
            stu=Student.objects.get(id=id)
            serialzer=StudentSerializer(stu)
            return Response(serialzer.data)
        stu=Student.objects.all()
        serialzer=StudentSerializer(stu,many=True)
        return Response(serialzer.data)

    if request.method=="POST":
        serialzer=StudentSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response({'msg':"Data Inserted Successfully"})
        return Response(serialzer.errors)

    if request.method=="PUT":
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serialzer=StudentSerializer(stu,data=request.data,partial=True)
        if serialzer.is_valid():
            serialzer.save()
            return Response({'msg':"Data updated successfully"})
        return Response(serialzer.errors)




