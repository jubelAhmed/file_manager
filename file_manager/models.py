from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FileManager(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	file = models.FileField(upload_to='uploads/', null=True)
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=500,null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class FileDeletedLog(models.Model):
	status = models.CharField(max_length=200)
	deleted_at = models.DateTimeField()

	def __str__(self):
		return self.status