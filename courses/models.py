import datetime

from django.db import models
from django.utils import timezone

def getCurrentTerm():
	month = timezone.now().month
	if month >= 9:
		return 'Fall'
	elif month >= 7:
		return 'Summer'
	elif month >= 5:
		return 'Spring'
	else:
		return 'Winter'

class School(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Department(models.Model):
	name = models.CharField(max_length=50)
	shortForm = models.CharField(max_length=15)
	school = models.ForeignKey(School, on_delete=models.CASCADE)

	def __str__(self):
		return self.school.name + ' Department of ' + self.name

class Course(models.Model):
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	code = models.CharField(max_length=10)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=250)
	year = models.IntegerField(default=timezone.now().year)
	term = models.CharField(max_length=10, default=getCurrentTerm())

	def __str__(self):
		return self.department.shortForm + ' ' + self.code + ': ' + self.name + ' ' + self.term + ' ' + str(self.year)

	def getFullCode(self):
		return self.department.shortForm + ' ' + self.code
	
