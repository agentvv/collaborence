from django.db import models
from django.forms import ModelForm
from django.utils.timezone import now
from django.contrib.auth.models import User
from slides.models import Slide

class Comment(models.Model):
    description = models.CharField(max_length=200)
    timeCreated = models.DateTimeField(default=now, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    slide = models.ForeignKey(Slide, on_delete=CASCADE, default=1)
    page = models.IntegerField(default=1)

    
    def __str__(self):
        return (self.author.username + ' ' + str(self.timeCreated))

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    timeCreated = models.DateTimeField(default=now, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return (self.author.username + ' ' + str(self.timeCreated))