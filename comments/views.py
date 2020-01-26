from django.forms import modelformset_factory
from django.shortcuts import render

from .models import Comment
from .forms import PartialCommentForm

def index(request):
    if request.method == 'POST':
        form  = PartialCommentForm(request.POST)
        comment = form.save(commit=False)
        comment.author = request.user
        comment.save()    
    else:
        comment = PartialCommentForm()
    
    return render(request, 'comments/create.html', {'form':comment})





