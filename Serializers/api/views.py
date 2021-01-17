from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.
#model object -Single Student Data

def student_details(request):
    stu=Student.objects.get(id=3)
    # print(stu)
    serializer=StudentSerializer(stu)
    # print(serializer)
    # print(serializer.data)
    # json_data=JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=True)


# QuerySet All student Data

def student_all(request):
    stu=Student.objects.all()
    print(stu)
    serializer=StudentSerializer(stu,many=True)
    print(serializer)
    print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')



