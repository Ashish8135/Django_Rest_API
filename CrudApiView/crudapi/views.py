from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer

# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def studentapi(request):
    if request.method=='GET':
        id=request.data.GET('id')
        if id is not None:
            stu=Student.objects.GET(id=id)
            serialzer=StudentSerializer(stu)
            return Response(serialzer.data)
        stu=Student.objects.all()
        serialzer=StudentSerializer(stu,many=True)
        return Response(serialzer.data)


