from django.shortcuts import render
from django.http import HttpResponse
from models import Question
import random

# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def questionsIndex(request):
	qcount = Question.objects.all().count()
	rand = random.randint(0, qcount-11)
	tquestions = Question.objects.all()[rand:rand+10]
	return render(request, 'questions.html', {'questions': tquestions})

def questionDetail(request, qid):
	ques = Question.objects.get(id=qid)
	#Stubbed for similar questions and trend questions
	qcount = Question.objects.all().count()
	rand1 = random.randint(0, qcount-5)
	rand2 = random.randint(0, qcount-5)
	sQs = Question.objects.all()[rand1:rand1+5]
	tQs = Question.objects.all()[rand2:rand2+5]
	return render(request, 'questiondetail.html', {'question': ques, 'similarquestions': sQs, 'trendquestions': tQs})

def prepare(request):
	cluster = []
	qcount = Question.objects.all().count()
	rand1 = random.randint(0, qcount-5)
	qs = Question.objects.all()[rand1:rand1+10]
	for i in range(10):
		cluster.append({'name': str(i+1), 'questions': [qs[i]]})
	print cluster
	return render(request, 'prepare.html', {'clusters': cluster})
