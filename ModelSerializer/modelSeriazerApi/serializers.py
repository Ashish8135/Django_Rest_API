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
        # extre_kwargs={'name':{'read_only':True},
        #                'roll':{'read_only':True}}

    #field level validation 
    def validation_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError("Sorry! Seat is already Full ")
        return value


    # object Level Validation
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='shubham' and ct.lower()=='gaya':
            raise serializers.ValidationError("City must be Gaya")
        return data





#Validation in ModelSerializer