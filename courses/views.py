from django.shortcuts import render
from django.http import FileResponse, Http404, HttpResponse

from .models import Course, School

def index(response):
    #course = course.objects.filter(department=)
    return render(response, 'course/course.html')

def view(response, num):
	#bla
	return render(response, 'slides/view.html', {"fileName":fileName});

def schools(response):
    schools = School.objects.all()
    return render(response, 'courses/schools.html', {"schools":schools})
