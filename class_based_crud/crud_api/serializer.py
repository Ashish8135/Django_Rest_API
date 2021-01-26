  

from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    branch=serializers.CharField(max_length=100)
    college=serializers.CharField(max_length=100)


    # Data create or insert into database or table by using create method
    def create(self,validate_data):
        return Student.objects.create(**validate_data)

    # for update data into database we must use update method in the serializer i.e
    def update(self,instance,validated_data):
        instance.id=validated_data.get('id',instance.id)
        print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.branch=validated_data.get('branch',instance.branch)
        instance.college=validated_data.get('college',instance.college)
        instance.save()
        return instance
    
    

