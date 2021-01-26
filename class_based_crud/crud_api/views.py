from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
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
    


    def post(self,request,*args,**kwargs):
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



    def put(self , request,*args,**kwargs):
        json_data=request.body     
        stream = io.BytesIO(json_data)   # get json data 
        # parse json data to python native data type
        python_data =JSONParser().parse(stream)   #converted json data to python native data type(dictionary)
        id= python_data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data updated successfully'}
            # converted python data into json 
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json') 
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json') 




    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'data deleted successfully'}
        # converted python data into json 
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json') 
        













        
