from django.db import models

class Comment(models.Model):
    description = models.CharField(max_length=200)
    time = models.DateTimeField('Date/Time created.')
    #author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return ("Comment Created @: " + self.time)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    time = models.DateTimeField('Date/Time created.')

    def __str__(self):
        return ("Replied to comment.")