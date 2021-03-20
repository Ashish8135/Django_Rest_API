from django.contrib import admin
from .models import (
    Region,Country,State,City,LocationData
)
# Register your models here.
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display=['id','name']
@admin.register(Country)
class RegionAdmin(admin.ModelAdmin):
    list_display=['id','name']
@admin.register(State)
class RegionAdmin(admin.ModelAdmin):
    list_display=['id','name']
@admin.register(City)
class RegionAdmin(admin.ModelAdmin):
    list_display=['id','name']
@admin.register(LocationData)
class RegionAdmin(admin.ModelAdmin):
    list_display=['id','name']