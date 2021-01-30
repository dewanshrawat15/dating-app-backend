from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Profile

class UserSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		return user

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password',
		)
		validators = [
			UniqueTogetherValidator(
				queryset=User.objects.all(),
				fields=['username', 'email']
			)
		]

class ProfileSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		profile = Profile.objects.create(validated_data)
		return profile

	class Meta:
		model = Profile
		fields = [
			'image_url_one',
			'image_url_two',
			'image_url_three',
			'image_url_four',
			'image_url_five',
			'image_url_six',
			'username'
		]