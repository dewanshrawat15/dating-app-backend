from rest_framework.serializers import Serializer, FileField, ListField
from .models import UserPhoto

# Serializers define the API representation.
class UploadSerializer(Serializer):
	file_uploaded = FileField()

	class Meta:
		model = UserPhoto
		fields = ['photo', 'uploaded_date', 'username']