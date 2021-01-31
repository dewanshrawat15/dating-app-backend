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

	def getProfileDetails(self, host):
		data = {
			"username": self.username,
			"image_url_one": self.getImageUrl(host, self.image_url_one),
			"image_url_two": self.getImageUrl(host, self.image_url_two),
			"image_url_three": self.getImageUrl(host, self.image_url_three),
			"image_url_four": self.getImageUrl(host, self.image_url_four),
			"image_url_five": self.getImageUrl(host, self.image_url_five),
			"image_url_six": self.getImageUrl(host, self.image_url_six)
		}
		return data

	def getImageUrl(self, host, img_rel_path):
		if len(img_rel_path) > 0:
			url = 'http://' + host + img_rel_path
			return url
		return ''

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


class MatchObj(models.Model):
	user_one = models.CharField(max_length=256)
	user_two = models.CharField(max_length=256)
	user_one_auth = models.BooleanField(blank=True)
	user_two_auth = models.BooleanField(blank=True)
	user_one_consensus = models.CharField(max_length=6, blank=True)
	user_two_consensus = models.CharField(max_length=6, blank=True)

	def __str__(self):
		string = self.user_one + " " + self.user_two
		return str(hash(string))


