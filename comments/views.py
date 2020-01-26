from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .models import Comment
from slides.models import Slide
from .models import Comment, Reply
from .forms import PartialCommentForm, PartialReplyForm

def newComment(request, num, num2):
    if request.method == 'POST':
        form  = PartialCommentForm(request.POST)
        comment = form.save(commit=False)
        comment.author = request.user
        comment.slide = Slide.objects.get(id=num)
        comment.page = num2
        comment.save()
        return redirect("/comments/viewComment/"+str(comment.id))    
    else:
        comment = PartialCommentForm()
        return render(request, 'comments/create.html', {'form':comment})

def viewComment(response, num):
    comment = Comment.objects.get(id=num)
    replies = Reply.objects.filter(comment=comment)
    return render(response, 'comments/viewComment.html', {"comment":comment, "replies":replies, "slide":comment.slide.id, "page":comment.page})

def createReply(request, num):
    
    if request.method == 'POST':
        form  = PartialReplyForm(request.POST)
        reply = form.save(commit=False)
        reply.author = request.user
        reply.comment = Comment.objects.get(id=num)
        reply.save()
        return redirect('/comments/viewComment/'+str(num))    
    else:
        reply = PartialCommentForm()
        return render(request, 'comments/createReply.html', {'form':reply})
    





