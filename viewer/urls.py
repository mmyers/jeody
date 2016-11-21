from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^questions/', views.questionsIndex, name="questionsIndex"),
	url(r'^$', views.index, name='index'),
]
