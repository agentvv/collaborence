from django.db import models

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=50)
    school_location = models.CharField(max_length=6, help_text='Example: ON, CA') # ON, CA
    
class Courses(models.Model):
    school_name = models.ForeignKey(School, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    course_department = models.CharField(max_length=50)
    course_term = models.CharField(max_length=10)
    course_id = models.CharField(max_length=10)