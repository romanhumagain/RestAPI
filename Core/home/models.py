from django.db import models


class Sports(models.Model):
  sports_type = models.CharField(max_length = 100)
  sports_name = models.CharField(max_length= 100)
  
  def __str__(self) -> str:
    return self.sports_name

class Persons(models.Model):
  sports = models.ForeignKey(Sports, null = True, blank = True, on_delete = models.CASCADE, related_name = "sports")
  name = models.CharField(max_length = 100)
  age = models.IntegerField()
  phone_number = models.IntegerField()
  
  def __str__(self):
    return self.name
  
class Student(models.Model):
  name = models.CharField(max_length = 100)
  email = models.EmailField(unique = True)
  phone_no = models.IntegerField(unique = True)
  address = models.CharField(max_length = 100)

  def clean(self) -> None:
    if self.phone_no <0:
      raise ValueError("Provide Valid Phone Number !")
  
  def __str__(self) -> str:
    return self.name