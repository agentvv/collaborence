from django.forms import modelformset_factory
from django.shortcuts import render

from .models import Comment
from .forms import CommentForm

def index(request):
    CommentFormSet = modelformset_factory(Comment, fields=('author', 'description'))
    if request.method == 'POST':
        formset = CommentFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = CommentFormSet()
    return render(request, 'comments/base.html', {'formset': formset})
