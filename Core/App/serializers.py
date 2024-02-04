from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import status

class UserRegistrationSerializer(serializers.Serializer):
  username = serializers.CharField()
  email = serializers.EmailField()
  password = serializers.CharField()
  
  def validate(self, data):
    if data['username']:
      if User.objects.filter(username = data['username']).exists():
        return serializers.ValidationError("Username Already Exists !")
    
    if data['email']:
      if User.objects.filter(email = data['email']).exists():
        return serializers.ValidationError("Email Already Taken !")
      
    return data
      
  
  def create(self, validated_data):
    user = User.objects.create(username = validated_data['username'], email = validated_data['email'])
    user.set_password(validated_data['password'])
    user.save()
    
    return validated_data
    
    
class LoginUserSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()   
  