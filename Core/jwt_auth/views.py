from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .serializer import UserSerializer, LoginSerializer

from django.contrib.auth import get_user_model
import jwt, datetime

from django.contrib.auth import authenticate


User = get_user_model()

class RegisterAPIView(APIView):
  def post(self,request):
    data = request.data
    serializer = UserSerializer(data = data)
    
    if serializer.is_valid():
      serializer.save()
      return Response({'message':"User successfully created !", 'data':[serializer.data]})
    
    return Response(serializer.errors)
  
class LoginAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                payload = {
                    'id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                    'iat': datetime.datetime.utcnow()
                }
                token = jwt.encode(payload, 'secret', algorithm='HS256')
                
                response = Response()
                response.set_cookie(key='jwt', value=token, httponly=True)
                
                response.data = {"message": "Successfully Logged In.", "token": token}
                
                return response
            else:
                raise AuthenticationFailed("Invalid email or password.")
        return Response(serializer.errors)
      
      
class UserAPIView(APIView):
  def get(self, request):
    token = request.COOKIES.get('jwt')
    
    if not token:
      raise AuthenticationFailed("Unauthenticated User")
    
    try:
      payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    
    except jwt.ExpiredSignatureError:
      raise AuthenticationFailed("Unauthenticated User")
    
    user = User.objects.filter(id = payload['id']).first()
    serializer = UserSerializer(user)
    
    return Response(serializer.data)
    
class LogoutUserAPI(APIView):
  def post(self, request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
      'message':'Successfully Logout  !'
    }
    
    return response
