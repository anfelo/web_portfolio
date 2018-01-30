from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.articles_list, name='list'),
    path('<str:topic>/', views.articles_by_topic, name='topiclist'),
    path('<str:topic>/<int:pk>/', views.article_detail, name='detail'),
]