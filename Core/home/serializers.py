from rest_framework import serializers

from .models import Persons

class PersonSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Persons
    
    # to include all fields
    fields = '__all__'
    
    # # to include selected field
    # fields = ["name", "age"]
    # # to exclude the specific field
    # exclude = ["phone_number"]