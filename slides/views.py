from django.shortcuts import render, redirect
from django.http import FileResponse, Http404, HttpResponse


from django.http import HttpResponseRedirect
from .forms import UploadSlideForm

from .models import Slide
from courses.models import Course
from comments.models import Comment

import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def view(response, num, page):
    try:
        slide = Slide.objects.get(pk=num)
        courseNum = slide.course.id
        fileName = 'slides/' + slide.fileName + '/' + slide.title + ' ' + str(page) +'.pdf'
        comments = Comment.objects.filter(slide=Slide.objects.get(id=num))
        return render(response, 'slides/view.html', {"fileName":fileName, "courseNum":courseNum, 'num': num, 'pageNum':page, 'comments':comments});
    except:
        raise Http404("Slides not found: " + 'slides/' + slide.fileName + '/' + slide.title + ' ' + str(page) +'.pdf')


def pdfSplitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    output = os.path.dirname(path)
 
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
 
        output_filename = output + '/{} {}.pdf'.format(fname, page+1)
 
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

def uploadSlide(request, num):
    course = Course.objects.get(id=num)
    courseCode = course.getFullCode()
    if request.method == 'POST':
        form = UploadSlideForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST['title']
            fileName = './slides/static/slides/' + title + '/' + title + '.pdf'
            try:
                os.mkdir('./slides/static/slides/'+title)
            except:
                return render(request,  'slides/upload.html', {'form': form, 'failed': True, 'course':courseCode, 'num':num})
            
            try:
                f = open(fileName, 'wb')
                f.write(request.FILES['file'].read())
                f.close()
                pdfSplitter(fileName)
                os.remove(fileName)
                slide = Slide(fileName=title, title=title, course=course)
                slide.save()
            except:
                raise Http404("write failed")
                
            return redirect("/home")
        else:
            return render(request,  'slides/upload.html', {'form': form, 'failed': True, 'course':courseCode, 'num':num})
    else:
        form = UploadSlideForm()
        
    return render(request, 'slides/upload.html', {'form': form, 'failed': False, 'course':courseCode, 'num':num})
