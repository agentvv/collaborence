from django.shortcuts import render, redirect
from django.http import FileResponse, Http404, HttpResponse

from .models import Course, School, Department

def index(response):
    #course = course.objects.filter(department=)
    return render(response, 'course/course.html')

def view(response, num):
	#bla
	return render(response, 'slides/view.html', {"fileName":fileName});

def schools(response):
    title = "Schools"
    schools = School.objects.all()
    section = "schools"
    return render(response, 'courses/base.html', {"title":title, "list":schools, "section":section})

def school(response, num):
    title = "Departments"
    departments = Department.objects.filter(school=School.objects.get(id=num))
    section ="departments"
    return render(response, 'courses/base.html', {"title":title, "list":departments, "section":section})

def department(response, num):
    title = "Courses"
    courses = Course.objects.filter(department=Department.objects.get(id=num))
    section = "add"
    return render(response, 'courses/base.html', {"title":title, "list":courses, "section":section})

def add(response, num):
    response.user.profile.courses.add(Course.objects.get(id=num))
    return redirect('/home')
