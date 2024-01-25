from rest_framework import serializers
from .models import Persons, Sports
import re

class SportSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sports
    fields = ["sports_name"]

class PersonSerializer(serializers.ModelSerializer):
  sports = SportSerializer()
  
  class Meta:
    model = Persons
    
    # to include all fields
    fields = '__all__'
    
    '''
    # to get the all the details of the foreign key linked table
    depth = 1
    '''
    # # to include selected field
    # fields = ["name", "age"]
    # # to exclude the specific field
    # exclude = ["phone_number"]
    
    
  # validating the fields
  
  # # validating by specifying the fileds
  # def validate_name(self, data):
  #   code to validate name
  
  # def validate_age(self, data):
  #   code to validate age
  
  # validating without specifying the fields
  def validate(self, data):
    
    # Define a regular expression pattern for special characters
    special_character_pattern = re.compile('[!@#$%^&*()_+{}\[\]:;<>,.?~\\/\|]')
    
    # Check if the name contains any special character or not 
    if bool(special_character_pattern.search(data["name"])):
        raise serializers.ValidationError("Name cannot contain any special characters!")

    # Check if age is less than 18
    if data['age'] < 18:
        raise serializers.ValidationError("Age cannot be less than 18 years old.")

    return data
