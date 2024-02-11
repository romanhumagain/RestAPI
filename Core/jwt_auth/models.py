from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):
  name = models.CharField(max_length = 100)
  email = models.EmailField(unique = True)
  password = models.CharField(max_length = 100)
  profile_image = models.ImageField(upload_to='profile')
  
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  
  username = None
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  
  objects = UserManager()
  
  def __str__(self) -> str:
    return self.email

