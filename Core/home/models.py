from django.db import models

class Persons(models.Model):
  name = models.CharField(max_length = 100)
  age = models.IntegerField()
  phone_number = models.IntegerField()
  
  def __str__(self):
    return self.name
  