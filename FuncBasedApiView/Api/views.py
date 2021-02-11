from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# @api_view()
# def hello(request):
#     return Response({'msg':'Hello World'})


@api_view(['GET','POST'])
def hello(request):
    if request.method=='GET':
        return Response({'msg':'THis is Get Request'})
    if request.method=='POST':
        print(request.data)
        return Response({'msg':'This is post request','data':request.data})