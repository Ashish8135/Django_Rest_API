from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt  
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
    





# Insert/Creat data into database

    if request.method=="POST":   # post request send to the server
        json_data=request.body     
        stream = io.BytesIO(json_data)   # get json data 
        # parse json data to python native data type
        python_data =JSONParser().parse(stream)   #converted json data to pytho native data type(dictionary)
        serializer=StudentSerializer(data=python_data) # converted python data type to complex 
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data inserted successfully'}
            # converted python data into json 
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json') 
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json') 

    




    




        
