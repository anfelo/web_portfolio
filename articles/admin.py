from django.contrib import admin

from .models import Article, Topic


class ArticleAdmin(admin.ModelAdmin):
	fields = ['topic', 'url_name', 'title', 'description', 'content']

	search_fields = ['title', 'description']

	list_filter = ['created_at', 'topic']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Topic)



