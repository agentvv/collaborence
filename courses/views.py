from django.shortcuts import render
from django.http import FileResponse, Http404, HttpResponse

from .models import Course

def index(response):
    #course = course.objects.filter(department=)
    return render(response, 'course/course.html')

def view(response, num):
	#bla
	return render(response, 'slides/view.html', {"fileName":fileName});
