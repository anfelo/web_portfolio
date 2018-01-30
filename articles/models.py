from django.db import models

# Create your models here.
class Topic(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class Article(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)
	description = models.TextField()
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	content = models.TextField(default='')

	def __str__(self):
		return self.title
