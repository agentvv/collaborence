from django.shortcuts import render
from django.http import FileResponse, Http404, HttpResponse

from .models import Comment

def index(response):
    #slides = Slide.objects.filter(course=)
    return render(response, 'comments/base.html')
