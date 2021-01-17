from django.contrib import admin
from crud_api import Student

# Register your models here.
@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city','branch','college']
