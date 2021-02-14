from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    model=Student
    fields=['id','name','roll','city']