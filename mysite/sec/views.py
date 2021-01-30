from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterApiView(APIView):

	permission_classes = [AllowAny]

	def get(self, format=None):
		data = {
			"error": True,
			"error_msg": "The GET request method for the user registration API is unavailable."
		}
		return Response(data, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid(raise_exception=ValueError):
			serializer.create(validated_data=request.data)
			Profile.objects.create(username=request.data['username'])
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response({
			"error": True,
			"error_msg": serializer.error_messages
		}, status=status.HTTP_400_BAD_REQUEST)