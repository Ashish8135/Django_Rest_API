from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializer import StudentSerialzer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer_data = StudentSerialzer(data = pythondata)
        if serializer_data.is_valid():
            serializer_data.save()
            res={'msg':'data created successfully'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data=JSONRenderer().render(serializer_data.errors)
        return HttpResponse(json_data,content_type="application/json")

