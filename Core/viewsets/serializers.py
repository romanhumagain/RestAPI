from rest_framework import serializers
from .models import Item, Comment, Product, Category, Review

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'
    
class ItemSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True, read_only=True)
  
  class Meta:
    model = Item
    fields = '__all__'
    
    
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'name', 'description']
    
class ProductSerializer(serializers.ModelSerializer):
  category = CategorySerializer(read_only = True)
  
  class Meta:
    model = Product
    fields = ['id', 'category', 'name', 'description', 'price']
    
class ReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'comment']