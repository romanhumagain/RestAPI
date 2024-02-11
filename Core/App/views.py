from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (UserRegistrationSerializer, 
                          LoginUserSerializer)
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

# to get our custom user model
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationAPIView(APIView):
  def post(self, request):
    data = request.data
    
    serializer = UserRegistrationSerializer(data = data)
    
    if not serializer.is_valid():
      return Response({'status': True, 'message': serializer.errors}, status= status.HTTP_400_BAD_REQUEST)
    
    serializer.save()
    user = User.objects.get(email = serializer.validated_data['email'])
    
    refresh = RefreshToken.for_user(user)  # creates the jwt token
    
    return Response({'status':True, 'message':'User Created Successfully', 'token_data':[{'refresh': str(refresh),
        'access': str(refresh.access_token)}]}, status=status.HTTP_201_CREATED)
    
class UserLoginAPIView(APIView):
  def post(self, request):
    data = request.data
    serializer = LoginUserSerializer(data= data)
    if serializer.is_valid():
      user = authenticate(email = serializer.data['email'], password = serializer.data['password'])
      
      if user is not None:
        token, _ = Token.objects.get_or_create(user = user)
        return Response({'status':True, 'message' : "Successfully Logged In.", 'token':str(token)}, status= status.HTTP_200_OK)
      
      return Response({'status':False, 'message' : "Invalid Credentisl"}, status= status.HTTP_400_BAD_REQUEST)
      
    
    
    