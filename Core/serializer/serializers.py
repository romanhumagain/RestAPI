from rest_framework.serializers import ModelSerializer
from .models import Book, Author, Review
from rest_framework import serializers

 
class ReviewSerializer(ModelSerializer):
  class Meta:
    model = Review
    fields = '__all__'
    
  def create(self, validated_data):
    review = Review.objects.create(
      book = validated_data['book'],
      reviewer_name = validated_data['reviewer_name'],
      rating = validated_data['rating'],
      comment = validated_data['comment']
    )
    
    return review
  
  def validate_rating(self, value):
    if value <1 or value >5:
      raise serializers.ValidationError("Rating must be between 1 and 5.")
    return value
  
  def validate(self, attrs):
    reviewer_name = attrs.get(['reviewer_name'])
    book_author_name = attrs['book'].author.name if attrs.get('book') else None
    
    if reviewer_name == book_author_name:
      raise serializers.ValidationError("Reviwer cannot be the same as the author name")    
    
    return attrs
  
 
class BookSerializer(ModelSerializer):
  reviews = ReviewSerializer(many = True, read_only = True)
  
  # to get only review comments
  # reviews_comment = serializers.SerializerMethodField(read_only = True)
  
  
  author_name = serializers.SerializerMethodField(read_only = True) 
  
  class Meta:
    model = Book
    fields = '__all__'
    
  def get_author_name(self, obj):
    return obj.author.name if obj.author else None
  
  
  # to get only review comments
  '''
  # def get_reviews_comment(self, obj):
  #   reviews_comments = [review.comment for review in obj.reviews.all()]
  #   return reviews_comments
    '''
    
class AuthorSerializer(ModelSerializer):
  books = BookSerializer(many = True, read_only = True)
 
  # # StringRelatedField may be used to represent the target of the relationship using its __str__ method.
  # books = serializers.StringRelatedField(many = True, read_only = True)
  
  # books = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
  
  class Meta:
    model = Author
    fields = '__all__'
    
# ============== USING DEPTH =======================


class AuthorSerializer(ModelSerializer):
  # books = BookSerializer(many = True, read_only = True)
 
  # # StringRelatedField may be used to represent the target of the relationship using its __str__ method.
  # books = serializers.StringRelatedField(many = True, read_only = True)
  
  # books = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
  
  class Meta:
    model = Author
    fields = '__all__'    
    depth = 1
    
class BookSerializer(ModelSerializer):
  
  class Meta:
    model = Book
    fields = '__all__'
    depth = 1
    

    