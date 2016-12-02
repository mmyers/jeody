from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
	text = models.CharField(max_length=1000)
	value = models.CharField(max_length=10)
	normal_value = models.CharField(max_length=10)
	answer = models.CharField(max_length=500)
	theRound = models.CharField(max_length=100)
	showNumber = models.IntegerField()
	airDate = models.DateTimeField()
	DBSCANJaccardDistance = models.IntegerField()
	DBSCANEuclideanDistance = models.IntegerField()
	DBSCANCosineDistance = models.IntegerField()
	DBSCANHammingDistance = models.IntegerField()
	category = models.ForeignKey(QuestionCategory)
	
class QuestionCategory(models.Model):
	category = models.CharField(max_length=100)
