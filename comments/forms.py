from django.forms import ModelForm
from .models import Comment

class PartialCommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['author']