from django.shortcuts import render, redirect

# Create your views here.
def index(response):
    if response.user.is_authenticated:
        return redirect('/home')
    return render(response, "home/base.html", {})

def home(response):
    userCourses = response.user.profile.courses.all()
    return render(response, "home/home.html", {"courses":userCourses})