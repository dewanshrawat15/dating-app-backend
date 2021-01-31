from django.shortcuts import render
from .serializers import UserSerializer, MatchSerializer, ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .models import Profile, MatchObj
from django.db.models import Q


class UserRegisterApiView(APIView):

	permission_classes = [AllowAny]

	def get(self, format=None):
		data = {
			"error": True,
			"message": "The GET request method for the user registration API is unavailable."
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
			"message": serializer.error_messages
		}, status=status.HTTP_400_BAD_REQUEST)


class MatchAPI(APIView):

	permission_classes = [IsAuthenticated]
	serializer_class = MatchSerializer

	def get(self, request):
		if request.user.is_authenticated:
			host = request.get_host()
			username = request.user.username
			profiles = Profile.objects.all()
			matches = MatchObj.objects.filter(Q(user_one=username) | Q(user_two=username))
			users_not_to_show = []
			for i in matches:
				if len(str(i.user_two_consensus)) > 0:
					users_not_to_show.append(i.user_two)
			details = []
			for i in profiles:
				profile_data = i.getProfileDetails(host)
				if profile_data['username'] != username:
					details.append(profile_data)
			for idx in range(len(details)):
				for blacklister in users_not_to_show:
					if details[idx]['username'] == blacklister:
						details.pop(idx)
			return Response({
				"error": False,
				"profiles": details
			}, status=status.HTTP_200_OK)
		else:
			return Response({
				"error": True,
				"message": "Unauthorized."
			}, status=status.HTTP_401_UNAUTHORIZED)

	def post(self, request):
		user_one = request.data['user_one']
		user_two = request.data['user_two']
		vote = request.data['match']
		if user_one == request.user.username or user_two == request.user.username:
			find_match = MatchObj.objects.filter(Q(user_one=user_one, user_two=user_two) | Q(user_one=user_two, user_two=user_one))
			if len(find_match) <= 0:
				match = MatchObj.objects.create(user_one=user_one, user_two=user_two, user_one_auth=False, user_two_auth=False, user_one_consensus='', user_two_consensus='')
				if request.user.username == user_one:
					match.user_one_auth = "True"
					if vote:
						match.user_one_consensus = "True"
					else:
						match.user_one_consensus = "False"
			else:
				match = MatchObj.objects.get(user_one=user_two, user_two=user_one)
				if request.user.username == user_one:
					match.user_two_auth = "True"
					if vote:
						match.user_two_consensus = "True"
					else:
						match.user_two_consensus = "False"
			match.save()
			return Response({
				"error": False,
				"message": "Match object created"
			}, status=status.HTTP_200_OK)
		else:
			return Response({
				"error": False
			}, status=status.HTTP_401_UNAUTHORIZED)