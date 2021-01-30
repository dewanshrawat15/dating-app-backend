from django.db import models
from django.utils import timezone
import os

# Create your models here.

def user_directory_path(username, filename):
	return 'user_{0}/{1}'.format(username, filename)

class UserPhoto(models.Model):
	photo = models.FileField(upload_to=user_directory_path, max_length=1024)
	uploaded_date = models.DateTimeField(default=timezone.now)
	username = models.CharField(max_length=64)

	def __str__(self):
		return self.username

	def delete(self, *args, **kwargs):
		self.photo.delete()
		super(UserPhoto, self).delete(*args, **kwargs)