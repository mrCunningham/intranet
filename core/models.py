from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	create_date = models.DateTimeField('date created')
	author = models.CharField(max_length=35)
	content = models.TextField('post content')
	
	def __str__(self):
		return self.title
	
