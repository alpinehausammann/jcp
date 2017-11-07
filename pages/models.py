from django.db import models


# Create your models here.
class Page(models.Model): #creates pages on website
	created_at = models.DateTimeField(auto_now_add = True)
	title = models.CharField(max_length = 255)
	main_content = models.TextField()
	
	def __str__(self):
		return self.title

class NewContent(models.Model): #add additional content to Pages
	title = models.CharField(max_length = 255)
	content = models.TextField()
	page = models.ForeignKey(Page,on_delete = models.CASCADE)
	order = models.IntegerField(default = 0)
	
	def Meta():
		ordering = ['order',]

	def __str__(self):
		return self.title

	
