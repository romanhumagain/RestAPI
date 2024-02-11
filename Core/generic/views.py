from rest_framework.generics import (
  ListAPIView, 
  RetrieveAPIView,
  CreateAPIView, 
  UpdateAPIView, 
  DestroyAPIView
)
from .models import Products
from .serializers import ProductSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class ListProductAPIView(ListAPIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  
  queryset = Products.objects.all()
  serializer_class = ProductSerializer
  
class CreateProductAPIView(CreateAPIView):
  queryset = Products.objects.all()
  serializer_class = ProductSerializer
  
  
class RetriveProduceAPIView(RetrieveAPIView):
  queryset = Products.objects.all()
  serializer_class = ProductSerializer
  
  lookup_field = "slug"
  
class UpdateProductAPIView(UpdateAPIView):
  queryset = Products.objects.all()
  serializer_class = ProductSerializer
  
  lookup_field = "slug"
  
class DestroyProductAPIView(DestroyAPIView):
  queryset = Products.objects.all()
  serializer_class = ProductSerializer
  
  lookup_field = "slug"
  
  
  

