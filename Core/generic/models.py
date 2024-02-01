from django.db import models

class Products(models.Model):
  slug = models.SlugField(unique = True)
  name = models.CharField(max_length = 200)
  price = models.IntegerField()
  
  def __str__(self) -> str:
    self.name