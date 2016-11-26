from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^questions/(?P<qid>[0-9]+)', views.questionDetail, name="questionDetail"),
	url(r'^questions/', views.questionsIndex, name="questionsIndex"),
	url(r'^prepare/', views.prepare, name="prepare"),
	url(r'^$', views.index, name='index'),
]
