  

from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    branch=serializers.CharField(max_length=100)
    college=serializers.CharField(max_length=100)

    # def create(self,validate_data):
    #     return 
    
    
