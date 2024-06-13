from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Item(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
  
  def __str__(self) -> str:
    return self.name
  
class Comment(models.Model):
  item = models.ForeignKey(Item, related_name='comments', on_delete=models.CASCADE)
  text = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self) -> str:
    return self.text[:20]
  

# ==== FOR THE E-COMMERCE WEBSITE SCENARIO ===========
class Category(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  
  def __str__(self) -> str:
    return self.name
  
class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE , related_name = 'products')
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
      return self.name
    
class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'