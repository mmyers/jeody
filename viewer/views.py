from django.shortcuts import render
from django.http import HttpResponse
from models import Question

# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def questionsIndex(request):
	tquestions = Question.objects.all()[:100]
	#print questions
	#return HttpResponse("Hello")
	return render(request, 'questions.html', {'questions': tquestions})
