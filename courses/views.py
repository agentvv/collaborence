from django.shortcuts import render, redirect
from django.http import FileResponse, Http404, HttpResponse

from .models import Course, School, Department
from slides.models import Slide
from .forms import CourseForm

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
    title = "Click a course to add it to your list of followed courses."
    courses = Course.objects.filter(department=Department.objects.get(id=num))
    section = "add"
    return render(response, 'courses/base.html', {"title":title, "list":courses, "section":section})

def add(response, num):
    response.user.profile.courses.add(Course.objects.get(id=num))
    return redirect('/home')

def course(response, num):
    title = "Click slides to view a slide deck"
    slides = Slide.objects.filter(course=Course.objects.get(id=num))
    section = "slides"
    return render(response, 'courses/slides.html', {"title":title, "list":slides, "section":section, 'num':num})

def createCourse(response):
    if response.method == 'POST':
        form = CourseForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = CourseForm()
    
    return render(response, 'courses/createCourse.html', {'form':form})
    


