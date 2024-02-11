from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import status

# to get our custom user model
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField()
  
  def validate(self, data):
    if data['email']:
      if User.objects.filter(email = data['email']).exists():
        return serializers.ValidationError("Email Already Taken !")
      
    return data
      
  
  def create(self, validated_data):
    user = User.objects.create(email = validated_data['email'])
    user.set_password(validated_data['password'])
    user.save()
    
    return validated_data
    
    
class LoginUserSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField()   
  