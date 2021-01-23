from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def student_api(request):
    if request.method=="GET":   # get/fetch data from database.
        json_data=request.body     # 
        stream = io.BytesIO(json_data)    
        # parse json data to python native data type
        python_data =JSONParser().parse(stream)   #used to parse json data to python native data type
        # store python data into variable
        id= python_data.get('id',None)
        # if data is present then fetch   
        if id is not None:
            stu=Student.objects.get(id=id)  # fetching single data from database
            #complex to python data type 
            serializer=StudentSerializer(stu) #complex to python data type
            json_data=JSONRenderer().render(serializer.data)  # python data type to json
            return HttpResponse(json_data,content_type='application/json') 

        stu=Student.objects.all()  # fetch all data from database
        # complex to python data type
        serializer=StudentSerializer(stu,many=True)  # complex to python data type
        json_data=JSONRenderer().render(serializer.data) # python data type to json
        return HttpResponse(json_data,content_type='application/json')




        
