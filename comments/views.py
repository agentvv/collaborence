from django.forms import modelformset_factory
from django.shortcuts import render
from .models import Comment

from .models import Comment
from .forms import PartialCommentForm

def newComment(request):
    if request.method == 'POST':
        form  = PartialCommentForm(request.POST)
        comment = form.save(commit=False)
        comment.author = request.user
        comment.save()    
    else:
        comment = PartialCommentForm()
    
    return render(request, 'comments/create.html', {'form':comment})

def viewComment(response, num):
    comment = Comment.objects.get(id=num)
    return render(response, 'comments/viewComment.html', {"comment":comment})
    




