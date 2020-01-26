from django.shortcuts import render

def index(response):
    return render(response, 'slides/base.html')
