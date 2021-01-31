from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import UserPhoto
from sec.models import Profile
from .serializers import UploadSerializer
import json
import base64
# Create your views here.

class ImageView(APIView):
	serializer_class = UploadSerializer
	permission_classes = [IsAuthenticated]

	def list(self, request):
		return Response("GET API")

	def get(self, request):
		username = request.user.username
		profile = Profile.objects.get(username=username)
		images = profile.getImagesMap()
		user_images = []
		for image in images:
			img_rel_path = images[image]
			if len(images[image]) > 0:
				host = request.get_host()
				url = 'http://' + host + img_rel_path
				user_images.append(url)
		return Response({
			"images": user_images
		}, status=status.HTTP_200_OK)

	def post(self, request):
		try:
			file_uploaded = request.FILES.get('user_image')
			associate_image_key = ''
			image_uploaded = False
			username = request.user.username
			profile = Profile.objects.get(username=username)
			images_map = profile.getImagesMap()
			for key in images_map:
				if len(images_map[key]) == 0:
					associate_image_key = key
					image_uploaded = True
					break
			if image_uploaded:
				user_photo = UserPhoto.objects.create(photo=file_uploaded, username=username)
				profile.putImageField(associate_image_key, user_photo.photo.url)
				return Response({
					"error": False,
					"message": 'Successful'
				}, status=status.HTTP_201_CREATED)
			else:
				return Response({
					"error": True,
					"message": 'Number of images that can be uploaded have exceeded'
				}, status=status.HTTP_200_OK)
		except Exception as e:
			return Response({
				"error": True,
				"message": str(e)
			}, status=status.HTTP_400_BAD_REQUEST)