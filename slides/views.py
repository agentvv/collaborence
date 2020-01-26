from django.shortcuts import render
from django.http import FileResponse, Http404, HttpResponse

from .models import Slide

def index(response):
    #slides = Slide.objects.filter(course=)
    return render(response, 'slides/slides.html')

def view(response, num):
    try:
        slide = Slide.objects.get(pk=num)
        fileName = 'slides/' + slide.fileName
        return render(response, 'slides/view.html', {"fileName":fileName});
    except:
        raise Http404("Slides not found")
