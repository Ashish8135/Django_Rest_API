from django.db import models

# Create your models here.
class Region(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    name=models.CharField(max_length=100)
    region=models.ForeignKey(Region,on_delete=models.CASCADE,related_name="country")
    
    def __str__(self):
        return self.name

class State(models.Model):
    name=models.CharField(max_length=100)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name="state")

    def __str__(self):
        return self.name

class City(models.Model):
    name=models.CharField(max_length=100)
    state=models.ForeignKey(State,on_delete=models.CASCADE,related_name="city")

    def __str__(self):
        return self.name

class LocationData(models.Model):
    name=models.CharField(max_length=100)
    city=models.ForeignKey(City,on_delete=models.CASCADE,related_name="location")

    def __str__(self):
        return self.name