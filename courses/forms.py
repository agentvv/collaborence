from django.forms import ModelForm
from .models import Course

class CourseForm(ModelForm):
    class Meta:
        model = Course
        exclude = ['year', 'term']