from django.db import models


class Department(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Post(models.Model):
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	create_date = models.DateTimeField('date created')
	author = models.CharField(max_length=35)
	content = models.TextField('post content')

	def __str__(self):
		return self.title
