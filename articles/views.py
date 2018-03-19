from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from . import models

# Create your views here.
def articles_list(request):
	articles = models.Article.objects.all().order_by('-created_at')
	return render(request, 'articles/article_list.html', {'articles': articles})


def articles_by_topic(request, topic):
	articles = models.Article.objects.filter(topic__name=topic).order_by('-created_at')
	return render(request, 'articles/article_list.html', {'articles': articles,
                                                          'topic': topic})


def article_detail(request, topic, url_name):
	article = get_object_or_404(models.Article, url_name=url_name)
	return render(request, 'articles/article_detail.html', {'article': article})


