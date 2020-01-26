from django.shortcuts import render

# Create your views here.
def index(response):
    return render(response, "home/base.html", {})

def home(response):
    return render(response, "home/home.html", {})