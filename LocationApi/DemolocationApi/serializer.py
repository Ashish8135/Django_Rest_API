from rest_framework import serializers
from .models import (
    Region,Country,State,City,LocationData
)

class RegionSerializer(serializers.ModelSerializer):
    country=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Region
        fields = ['id','name','country']
    
class CountrySerializer(serializers.ModelSerializer):
    state=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Country
        fields = ['id','name','state']


class StateSerializer(serializers.ModelSerializer):
    city=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = State
        fields = ['id','name','city']

class CitySerializer(serializers.ModelSerializer):
    location=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = City
        fields = ['id','name','location']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationData
        fields = '__all__'
