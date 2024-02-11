from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'name', 'email', 'password']
    
    extra_kwargs = {
      'password':{'write_only':True}
    }
    
  def create(self, validated_data):
    password = validated_data.pop('password', None)
    
    user_instance = self.Meta.model(**validated_data)
    
    if password is not None:
      user_instance.set_password(password)
      
    user_instance.save()
    
    return user_instance
  
  
class LoginSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField()   
  