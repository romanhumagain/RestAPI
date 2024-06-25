from django.shortcuts import render
from rest_framework import generics
from .models import Book, Review, Author
from .serializers import BookSerializer, ReviewSerializer, AuthorSerializer


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    
class BookListCreateAPIView(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  
  
class ReviewListCreateAPIView(generics.ListCreateAPIView):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
  
class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
  

