from django.forms import ModelForm
from .models import Comment, Reply

class PartialCommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['author']

class PartialReplyForm(ModelForm):
    class Meta:
        model = Reply
        exclude = ['author', 'comment']