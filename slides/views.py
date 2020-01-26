from django.shortcuts import render, redirect
from django.http import FileResponse, Http404, HttpResponse


from django.http import HttpResponseRedirect
from .forms import UploadSlideForm

from .models import Slide
from courses.models import Course

import os.path

def view(response, num):
    try:
        slide = Slide.objects.get(pk=num)
        courseNum = slide.course.id
        fileName = 'slides/' + slide.fileName
        return render(response, 'slides/view.html', {"fileName":fileName, "courseNum":courseNum});
    except:
        raise Http404("Slides not found")
    

def uploadSlide(request, num):
    course = Course.objects.get(id=num)
    courseCode = course.getFullCode()
    if request.method == 'POST':
        form = UploadSlideForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST['title']
            fileName = './slides/static/slides/' + title + '.pdf'
            try:
                if not os.path.exists(fileName):
                    try:
                        f = open(fileName, 'wb')
                        f.write(request.FILES['file'].read())
                        f.close()
                        slide = Slide(fileName=title+'.pdf', title=title, course=course)
                        slide.save()
                    except:
                        raise Http404("write failed")
                        
                    return redirect("/home")
                else:
                    return render(request,  'slides/upload.html', {'form': form, 'failed': True, 'course':courseCode, 'num':num})
            except:
                raise Http404("os path failed")
    else:
        form = UploadSlideForm()
        
    return render(request, 'slides/upload.html', {'form': form, 'failed': False, 'course':courseCode, 'num':num})
