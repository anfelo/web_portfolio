from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from . import models

# Create your views here.
def articles_list(request):
	articles = models.Article.objects.all()
	return render(request, 'articles/article_list.html', {'articles': articles})


def articles_by_topic(request, topic):
	topic_pk = get_object_or_404(models.Topic, name=topic)
	articles = models.Article.objects.filter(topic=topic_pk)
	return render(request, 'articles/article_list.html', {'articles': articles,
                                                          'topic': topic})


def article_detail(request, topic, pk):
	article = get_object_or_404(models.Article, pk=pk)
	return render(request, 'articles/article_detail.html', {'article': article})


