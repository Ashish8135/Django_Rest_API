from .models import Student
from rest_framework import serializers


# BY using seriazer class we use serializer
# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=100)
#     roll=serializers.IntegerField()
#     course=serializers.CharField(max_length=100)
#     branch=serializers.CharField(max_length=100)
#     city=serializers.CharField(max_length=100)
#     college=serializers.CharField(max_length=100)


# By using ModelSerializer Method predefind automitically

class StudentSerializer(serializers.ModelSerializer):
    # 1.Way :: name=serializers.CharField(read_only=True)  
    class Meta:
        model=Student
        fields=['name','roll','course','branch','city','college']

        # for multiple fields we use jusk like that we do by three ways
        # 2.Way :: read_only_fields= ['name','roll']
        # 3.Way ::Given below
        extre_kwargs={'name':{'read_only':True},
                       'roll':{'read_only':True}}




#Validation in ModelSerializer