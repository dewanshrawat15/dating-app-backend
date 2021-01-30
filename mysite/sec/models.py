from django.db import models

# Create your models here.
class Profile(models.Model):
	image_url_one = models.CharField(max_length=512, blank=True)
	image_url_two = models.CharField(max_length=512, blank=True)
	image_url_three = models.CharField(max_length=512, blank=True)
	image_url_four = models.CharField(max_length=512, blank=True)
	image_url_five = models.CharField(max_length=512, blank=True)
	image_url_six = models.CharField(max_length=512, blank=True)
	username = models.CharField(max_length=128)

	def __str__(self):
		return self.username

	def getImagesMap(self):
		data = {
			"image_url_one": self.image_url_one,
			"image_url_two": self.image_url_two,
			"image_url_three": self.image_url_three,
			"image_url_four": self.image_url_four,
			"image_url_five": self.image_url_five,
			"image_url_six": self.image_url_six
		}
		return data

	def putImageField(self, key, image_url):
		if key == 'image_url_one':
			self.image_url_one = image_url
		elif key == 'image_url_two':
			self.image_url_two = image_url
		elif key == 'image_url_three':
			self.image_url_three = image_url
		elif key == 'image_url_four':
			self.image_url_four = image_url
		elif key == 'image_url_five':
			self.image_url_five = image_url
		elif key == 'image_url_six':
			self.image_url_six = image_url
		self.save()