from django.db import models
from django.utils.timezone import now

class Comment(models.Model):
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    timeCreated = models.DateTimeField(default=now, editable=False)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return ("Comment Created @: " + self.timeCreated)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    timeCreated = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return ("Replied to comment.")
