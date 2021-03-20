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
    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationData
        fields = '__all__'
