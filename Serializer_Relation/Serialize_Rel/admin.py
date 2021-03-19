from django.contrib import admin
from .models import Singer
from Serialize_Rel.models import Song
# Register your models here.
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display=['id','name','gender']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=['id','title','singer','duration']

