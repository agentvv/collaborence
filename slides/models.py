from django.db import models

# Create your models here.
class Slide(models.Model):
    title = models.CharField(max_length=30)
    fileName = models.CharField(max_length=50)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    
    def __str__ (): 
        return self.name