from .models import Comment
from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(label='Name: ', max_length=20)
    description = forms.CharField(label='Comment: ', max_length=250)
    